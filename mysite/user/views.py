from django.shortcuts import render
from django.urls import reverse

from .models import Person, Vessels, Type, Fuel
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.datastructures import MultiValueDictKeyError
import hashlib
from .forms import Entry, FindVessel, FilterVessel, AddType, AddVessel


# Create your views here.

def find_vessels(request, vessels, form_find_vessel):
    if form_find_vessel.is_valid():
        find_name = form_find_vessel.cleaned_data.get('find_name')
        find_IMO = form_find_vessel.cleaned_data.get('IMO')
        if find_name != '':
            vessels = vessels.filter(name__contains=find_name)
            if find_IMO is not None:
                vessels = vessels.filter(IMO__contains=find_IMO)
        else:
            if find_IMO is not None:
                vessels = vessels.filter(IMO__contains=find_IMO)
    return vessels


def filter_vessels(request, vessels, filter_form):
    if filter_form.is_valid():
        type_filter = request.POST.get('type_filter[]')
        name_filter = filter_form.cleaned_data.get('name')
        IMO_filter = filter_form.cleaned_data.get('IMO')
        if name_filter != '':
            vessels = vessels.filter(name__contains=name_filter)
            if IMO_filter is not None:
                vessels = vessels.filter(IMO__contains=IMO_filter)
            if type_filter:
                vessels = vessels.filter(type__type__in=type_filter)

        else:
            if IMO_filter is not None:
                vessels = vessels.filter(IMO__contains=IMO_filter)
                if type_filter:
                    vessels = vessels.filter(type__type__in=type_filter)
            else:
                if type_filter:
                    vessels = vessels.filter(type__type__in=type_filter)
    return vessels


def add_type_vessel(add_type_form):
    new_type = add_type_form.cleaned_data.get('type')
    try:
        Type.objects.get(type=new_type)
    except Type.DoesNotExist:
        type_new = Type(type=new_type)
        type_new.save()


def add_vessel(add_vessel_form, photo):
    name_ship = add_vessel_form.cleaned_data.get('name')
    IMO_ship = add_vessel_form.cleaned_data.get('IMO')
    type_ship = add_vessel_form.cleaned_data.get('type')
    user_ship = add_vessel_form.cleaned_data.get('user')
    name_in_en = add_vessel_form.cleaned_data.get('name_in_en')
    try:
        Vessels.objects.get(name=name_ship, IMO=IMO_ship)
    except Vessels.DoesNotExist:
        user_name_add_ship = Person.objects.get(name=user_ship)
        ship_type = Type.objects.get(type=type_ship)
        # try:
        #     photo = add_vessel_form.cleaned_data['photo']
        #     new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
        #                        photo=photo.image, name_in_en=name_in_en)
        # except MultiValueDictKeyError:
        #     new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
        #                        name_in_en=name_in_en)
        if photo is not None:
            new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
                               photo=photo, name_in_en=name_in_en)
        else:
            new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
                               name_in_en=name_in_en)
    new_ship.save()
    name_ship = Vessels.objects.get(name=name_ship)
    fuel = Fuel(vessels=name_ship)
    fuel.save()


def index(request):
    if request.method == 'POST':
        form = Entry(request.POST)
        if form.is_valid():
            login = request.POST.get('login')
            check_password = request.POST.get('password')
            h2 = hashlib.md5(check_password.encode())
            check_password = h2.hexdigest()
            user = Person.objects.filter(login=login).filter(password=check_password).count()
            user_type = Person.objects.filter(login=login).filter(password=check_password)
            if user == 0:
                return render(request, 'user/index.html')
            else:
                if user_type.filter(type='user'):
                    request.session['login'] = login
                    return HttpResponseRedirect('/user/')

                elif user_type.filter(type='admin'):
                    request.session['login'] = login
                    return HttpResponseRedirect('/Administrator/')
                else:
                    request.session['login'] = login
                    return HttpResponseRedirect('/creator/')
    else:
        form = Entry()
    return render(request, 'user/index.html', {'form': form})


def user(request):
    login = request.session['login']
    user_flag = Person.objects.filter(login=login).filter(type='user').count()
    if user_flag == 0:
        return HttpResponseRedirect('/')
    form_find_vessel = FindVessel()
    filter_form = FilterVessel()
    user_name = Person.objects.filter(login=login)
    vessels = Vessels.objects.filter(user__login=login)
    all_type = Type.objects.all().values()
    paginator = Paginator(vessels, 5)
    page = request.GET.get('page')
    try:
        all_ship_page = paginator.page(page)
    except PageNotAnInteger:
        all_ship_page = paginator.page(1)
    except EmptyPage:
        all_ship_page = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        if 'find_ship' in request.POST:
            form_find_vessel = FindVessel(request.POST)
            vessels = find_vessels(request, vessels, form_find_vessel)
        if 'filter_button' in request.POST:
            filter_form = FilterVessel(request.POST)
            vessels = filter_vessels(request, vessels, filter_form)
        paginator = Paginator(vessels, 5)
        page = request.GET.get('page')
        try:
            all_ship_page = paginator.page(page)
        except PageNotAnInteger:
            all_ship_page = paginator.page(1)
        except EmptyPage:
            all_ship_page = paginator.page(paginator.num_pages)
    return render(request, 'user/user.html',
                  context={"vessels": vessels, 'all_type': all_type, 'user_name': user_name,
                           'all_ship_page': all_ship_page, 'form_find_vessel': form_find_vessel,
                           'filter_form': filter_form})

    return HttpResponseRedirect('')


def admin(request):
    login = request.session['login']
    user_flag = Person.objects.filter(login=login).filter(type='admin').count()
    if user_flag == 0:
        return HttpResponseRedirect('/')
    add_vessel_form = AddVessel()
    form_find_vessel = FindVessel()
    filter_form = FilterVessel()
    add_type_form = AddType()
    user_name = Person.objects.filter(login=login)
    vessels = Vessels.objects.all()
    all_type = Type.objects.all().values()
    all_users = Person.objects.filter(type='user').values()
    paginator = Paginator(Vessels.objects.all(), 5)
    id_change = request.GET.get('id')
    change_change = Vessels.objects.filter(id=id_change)
    page = request.GET.get('page')
    try:
        all_ship_page = paginator.page(page)
    except PageNotAnInteger:
        all_ship_page = paginator.page(1)
    except EmptyPage:
        all_ship_page = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        if 'AddTypeButton' in request.POST:
            add_type_form = AddType(request.POST)
            if add_type_form.is_valid():
                add_type_vessel(add_type_form)
            return HttpResponseRedirect('/Administrator/')
        if 'AddShipButton' in request.POST:
            add_vessel_form = AddVessel(request.POST, request.FILES)
            if add_vessel_form.is_valid():
                try:
                    photo = request.FILES['photo']
                except MultiValueDictKeyError:
                    photo = None
                add_vessel(add_vessel_form, photo)
            return HttpResponseRedirect('/Administrator/')
        if 'find_ship' in request.POST:
            form_find_vessel = FindVessel(request.POST)
            vessels = find_vessels(request, vessels, form_find_vessel)
        if 'filter_button' in request.POST:
            filter_form = FilterVessel(request.POST)
            vessels = filter_vessels(request, vessels, filter_form)
        paginator = Paginator(vessels, 5)
        page = request.GET.get('page')
        try:
            all_ship_page = paginator.page(page)
        except PageNotAnInteger:
            all_ship_page = paginator.page(1)
        except EmptyPage:
            all_ship_page = paginator.page(paginator.num_pages)
    id_change = request.GET.get('id')
    change_change = Vessels.objects.filter(id=id_change)
    return render(request, 'user/admin.html', context={"vessels": vessels, 'all_type': all_type, 'all_users': all_users,
                                                       'user_name': user_name, 'all_ship_page': all_ship_page,
                                                       'change': change_change, 'form_find_vessel': form_find_vessel,
                                                       'filter_form': filter_form, 'add_type_form': add_type_form,
                                                       'add_vessel_form': add_vessel_form}
                  )

    # return HttpResponseRedirect('')


def creator_example(request):
    login = request.session['login']
    user_flag = Person.objects.filter(login=login).filter(type='creator').count()
    if user_flag == 0:
        return HttpResponseRedirect('/')
    else:
        user_name = Person.objects.filter(login=login)
        if request.method == 'POST':
            if 'users_button' in request.POST:
                return HttpResponseRedirect('/creator/users/')
            if 'vessels_button' in request.POST:
                return HttpResponseRedirect('/creator/vessels/')
    return render(request, 'user/example_creator.html', {'user_name': user_name})


def creator_vessels(request):
    login = request.session['login']
    user_flag = Person.objects.filter(login=login).filter(type='creator').count()
    if user_flag == 0:
        return HttpResponseRedirect('/')
    else:
        user_name = Person.objects.filter(login=login)
        vessels = Vessels.objects.all()
        all_type = Type.objects.all().values()
        all_users = Person.objects.all().values()
        paginator = Paginator(Vessels.objects.all(), 5)
        page = request.GET.get('page')
        try:
            all_ship_page = paginator.page(page)
        except PageNotAnInteger:
            all_ship_page = paginator.page(1)
        except EmptyPage:
            all_ship_page = paginator.page(paginator.num_pages)
        if request.method == 'POST':
            if 'AddTypeButton' in request.POST:
                new_type = request.POST.get('New_type')
                try:
                    type_new = Type.objects.get(type=new_type)
                except Type.DoesNotExist:
                    type_new = Type(type=new_type)
                    type_new.save()
                return HttpResponseRedirect('/creator/vessels/')
            if 'AddShipButton' in request.POST:
                name_ship = request.POST.get('name_add_ship')
                IMO_ship = request.POST.get('IMO_add_ship')
                type_ship = request.POST.get('type_add_ship')
                user_ship = request.POST.get('user_add_ship')
                name_in_en = request.POST.get('name_in_en')
                if IMO_ship != '':
                    try:
                        new_ship = Vessels.objects.get(name=name_ship, IMO=IMO_ship)
                    except Vessels.DoesNotExist:
                        user_name_add_ship = Person.objects.get(name=user_ship)
                        ship_type = Type.objects.get(type=type_ship)
                        try:
                            photo = request.FILES['photo']
                            new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
                                               photo=photo, name_in_en=name_in_en)
                            new_ship.save()
                            name_ship = Vessels.objects.get(name=name_ship)
                            fuel = Fuel(vessels=name_ship, b_r='0', b_b='0', b_c='0', N='0', Q='0', V='0', C='0',
                                        K='0', X='0', E='0')
                            fuel.save()
                        except MultiValueDictKeyError:
                            new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
                                               name_in_en=name_in_en)
                            new_ship.save()
                            name_ship = Vessels.objects.get(name=name_ship)
                            fuel = Fuel(vessels=name_ship, b_r='0', b_b='0', b_c='0', N='0', Q='0', V='0', C='0',
                                        K='0', X='0', E='0')
                            fuel.save()
                else:
                    IMO_ship = 0
                    try:
                        new_ship = Vessels.objects.get(name=name_ship, IMO=IMO_ship)
                    except Vessels.DoesNotExist:
                        user_name_add_ship = Person.objects.get(name=user_ship)
                        # vessels = Vessels.objects.all().values()
                        ship_type = Type.objects.get(type=type_ship)
                        try:
                            photo = request.FILES['photo']
                            new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
                                               photo=photo, name_in_en=name_in_en)
                            new_ship.save()
                            name_ship = Vessels.objects.get(name=name_ship)
                            fuel = Fuel(vessels=name_ship, b_r='0', b_b='0', b_c='0', N='0', Q='0', V='0', C='0',
                                        K='0', X='0', E='0')
                            fuel.save()
                        except MultiValueDictKeyError:
                            new_ship = Vessels(name=name_ship, IMO=IMO_ship, user=user_name_add_ship, type=ship_type,
                                               name_in_en=name_in_en)
                            new_ship.save()
                            name_ship = Vessels.objects.get(name=name_ship)
                            fuel = Fuel(vessels=name_ship, b_r='0', b_b='0', b_c='0', N='0', Q='0', V='0', C='0',
                                        K='0', X='0', E='0')
                            fuel.save()
                return HttpResponseRedirect('/creator/vessels/')
            if 'find_ship' in request.POST:
                find_name = request.POST.get('find_name')
                find_IMO = request.POST.get('IMO_find')
                if find_name != '':
                    vessels = Vessels.objects.filter(name__contains=find_name)
                    if find_IMO != '':
                        vessels = vessels.filter(IMO__contains=find_IMO)
                else:
                    if find_IMO != '':
                        vessels = Vessels.objects.filter(IMO__contains=find_IMO)
                paginator = Paginator(vessels, 5)
                page = request.GET.get('page')
                try:
                    all_ship_page = paginator.page(page)
                except PageNotAnInteger:
                    all_ship_page = paginator.page(1)
                except EmptyPage:
                    all_ship_page = paginator.page(paginator.num_pages)
            if 'filter_button' in request.POST:
                type_filter = request.POST.getlist('type_filter[]')
                name_filter = request.POST.get('name_filter')
                IMO_filter = request.POST.get('IMO_filter')
                if name_filter != '':
                    vessels = Vessels.objects.filter(name__contains=name_filter)
                    if IMO_filter != '':
                        vessels = vessels.filter(IMO__contains=IMO_filter)
                    if type_filter:
                        vessels = vessels.filter(type__type__in=type_filter)

                else:
                    if IMO_filter != '':
                        vessels = Vessels.objects.filter(IMO__contains=IMO_filter)
                        if type_filter:
                            vessels = vessels.filter(type__type__in=type_filter)
                    else:
                        if type_filter:
                            vessels = vessels.filter(type__type__in=type_filter)
                paginator = Paginator(vessels, 5)
                page = request.GET.get('page')
                try:
                    all_ship_page = paginator.page(page)
                except PageNotAnInteger:
                    all_ship_page = paginator.page(1)
                except EmptyPage:
                    all_ship_page = paginator.page(paginator.num_pages)
        id_change = request.GET.get('id')
        change_change = Vessels.objects.filter(id=id_change)
        if request.method == 'POST':
            if 'changeButton' in request.POST:
                id = request.GET.get('id')
                name_ship = request.POST.get('name_change_ship')
                IMO_ship = request.POST.get('IMO_change_ship')
                type_ship = request.POST.get('type_change_ship')
                user_ship = request.POST.get('user_change_ship')
                new_type = Type.objects.get(type=type_ship)
                new_user = Person.objects.get(name=user_ship)
                vessels = Vessels.objects.get(id=id)
                if IMO_ship != '':
                    vessels.name = name_ship
                    vessels.IMO = IMO_ship
                    vessels.type = new_type
                    vessels.user = new_user
                    vessels.save()
                else:
                    vessels.name = name_ship
                    vessels.IMO = 0
                    vessels.type = new_type
                    vessels.user = new_user
                    vessels.save()

                return HttpResponseRedirect('/creator/vessels/')
    return render(
        request, 'user/creator_vessels.html', context={"vessels": vessels, 'all_type': all_type, 'user_name': user_name,
                                                       'all_users': all_users, 'all_ship_page': all_ship_page,
                                                       'change': change_change})


def creator_users(request):
    login = request.session['login']
    user_flag = Person.objects.filter(login=login).filter(type='creator').count()
    if user_flag == 0:
        return HttpResponseRedirect('/')
    else:
        user_name = Person.objects.filter(login=login)
        all_users = Person.objects.all()
        paginator = Paginator(Person.objects.all(), 5)
        page = request.GET.get('page')
        try:
            all_users_page = paginator.page(page)
        except PageNotAnInteger:
            all_users_page = paginator.page(1)
        except EmptyPage:
            all_users_page = paginator.page(paginator.num_pages)
        if request.method == 'POST':
            if 'user_filter_button' in request.POST:
                filter_user_name = request.POST.get('nameUserFilter')
                type_user = request.POST.getlist('type_User_filter[]')
                if filter_user_name != '':
                    all_users = Person.objects.filter(name__contains=filter_user_name)
                    if type_user:
                        all_users = all_users.filter(type__in=type_user)
                else:
                    if type_user:
                        all_users = all_users.filter(type__in=type_user)

                paginator = Paginator(all_users, 5)
                page = request.GET.get('page')
                try:
                    all_users_page = paginator.page(page)
                except PageNotAnInteger:
                    all_users_page = paginator.page(1)
                except EmptyPage:
                    all_users_page = paginator.page(paginator.num_pages)
            if 'Find_user_button' in request.POST:
                find_user = request.POST.get('nameUserFind')
                all_users = Person.objects.filter(name__contains=find_user)
                paginator = Paginator(all_users, 5)
                page = request.GET.get('page')
                try:
                    all_users_page = paginator.page(page)
                except PageNotAnInteger:
                    all_users_page = paginator.page(1)
                except EmptyPage:
                    all_users_page = paginator.page(paginator.num_pages)
            if 'add_user' in request.POST:
                firstname = request.POST.get('firstUserAdd')
                secondname = request.POST.get('secondnameUserAdd')
                name = firstname + ' ' + secondname
                login_add = request.POST.get('loginUserAdd')
                type = request.POST.get('type_user_add')
                new_password = request.POST.get('result')
                h_pass = hashlib.md5(new_password.encode())
                new_password = h_pass.hexdigest()
                try:
                    new_user = Person.objects.get(login=login_add)
                except Person.DoesNotExist:
                    new_user = Person(name=name, login=login_add, password=new_password, type=type,
                                      first_name=firstname,
                                      second_name=secondname)
                    new_user.save()
                return HttpResponseRedirect('/creator/users/')
        id_change = request.GET.get('id')
        change_change = Person.objects.filter(id=id_change)
        if request.method == 'POST':
            if 'changeButton' in request.POST:
                id = request.GET.get('id')
                update_user = Person.objects.get(id=id)
                update_user.first_name = request.POST.get('first_name_change_person')
                update_user.second_name = request.POST.get('secondname_change_person')
                update_user.name = update_user.first_name + ' ' + update_user.second_name
                update_user.type = request.POST.get('type_change_person')
                update_user.save()
                return HttpResponseRedirect('/creator/users/')
    return render(request, 'user/creator_users.html', context={'all_users': all_users, 'user_name': user_name,
                                                               'all_users_page': all_users_page,
                                                               'change': change_change})


def exit(request):
    try:
        del request.session['login']
    except KeyError:
        pass
    return HttpResponseRedirect('')


def change(request):
    login = request.session['login']
    person = Person.objects.filter(login=login)
    if request.method == 'POST':
        if 'save_change' in request.POST:
            person = Person.objects.get(login=login)
            person.first_name = request.POST.get('first_name')
            person.second_name = request.POST.get('second_name')
            person.name = person.first_name + ' ' + person.second_name
            new_password = request.POST.get('password')
            h = hashlib.md5(new_password.encode())
            p = h.hexdigest()
            if new_password != '':
                person.password = p
            try:
                person.photo = request.FILES['photo']
            except MultiValueDictKeyError:
                person.photo = person.photo
            person.save()
            return HttpResponseRedirect('/redact/')
    return render(request, 'user/change.html', context={'person': person})


def delete_vesselse(request, id):
    vessels = Vessels.objects.get(id=id)
    vessels.delete()
    return HttpResponseRedirect('/Administrator/')


def show_person_vessels(request, id):
    login = request.session['login']
    user_name = Person.objects.filter(login=login)
    vessels = Vessels.objects.filter(user__id=id)
    all_type = Type.objects.all().values()
    paginator = Paginator(vessels, 5)
    page = request.GET.get('page')
    try:
        all_ship_page = paginator.page(page)
    except PageNotAnInteger:
        all_ship_page = paginator.page(1)
    except EmptyPage:
        all_ship_page = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        if 'find_ship' in request.POST:
            find_name = request.POST.get('find_name')
            find_IMO = request.POST.get('IMO_find')
            if find_name != '':
                vessels = vessels.filter(name__contains=find_name)
                if find_IMO != '':
                    vessels = vessels.filter(IMO__contains=find_IMO)
                else:
                    if find_IMO != '':
                        vessels = vessels.filter(IMO__contains=find_IMO)
            paginator = Paginator(vessels, 5)
            page = request.GET.get('page')
            try:
                all_ship_page = paginator.page(page)
            except PageNotAnInteger:
                all_ship_page = paginator.page(1)
            except EmptyPage:
                all_ship_page = paginator.page(paginator.num_pages)
        if 'filter_button' in request.POST:
            type_filter = request.POST.getlist('type_filter[]')
            name_filter = request.POST.get('name_filter')
            IMO_filter = request.POST.get('IMO_filter')

            if name_filter != '':
                vessels = vessels.filter(name__contains=name_filter)
                if IMO_filter != '':
                    vessels = vessels.filter(IMO__contains=IMO_filter)
                if type_filter:
                    vessels = vessels.filter(type__type__in=type_filter)

            else:
                if IMO_filter != '':
                    vessels = vessels.filter(IMO__contains=IMO_filter)
                    if type_filter:
                        vessels = vessels.filter(type__type__in=type_filter)
                else:
                    if type_filter:
                        vessels = vessels.filter(type__type__in=type_filter)
        paginator = Paginator(vessels, 5)
        page = request.GET.get('page')
        try:
            all_ship_page = paginator.page(page)
        except PageNotAnInteger:
            all_ship_page = paginator.page(1)
        except EmptyPage:
            all_ship_page = paginator.page(paginator.num_pages)
    return render(request, 'user/user.html',
                  context={"vessels": vessels, 'all_type': all_type, 'user_name': user_name,
                           'all_ship_page': all_ship_page})


def delete_vesselse_creator(request, id):
    vessels = Vessels.objects.get(id=id)
    vessels.delete()
    return HttpResponseRedirect('/creator/vessels/')


def delete_user_creator(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect('/creator/users/')


def change_vessels(request, id):
    change_change = Vessels.objects.filter(id=id)
    login = request.session['login']
    user_name = Person.objects.filter(login=login)
    all_type = Type.objects.all().values()
    all_users = Person.objects.filter(type='user').values()
    if request.method == 'POST':
        if 'changeButton' in request.POST:
            name_ship = request.POST.get('name_change_ship')
            IMO_ship = request.POST.get('IMO_change_ship')
            type_ship = request.POST.get('type_change_ship')
            user_ship = request.POST.get('user_change_ship')
            new_type = Type.objects.get(type=type_ship)
            new_user = Person.objects.get(name=user_ship)
            vessels = Vessels.objects.get(id=id)
            if IMO_ship != '':
                vessels.name = name_ship
                vessels.IMO = IMO_ship
                vessels.type = new_type
                vessels.user = new_user
                try:
                    vessels.photo = request.FILES['photo']
                except MultiValueDictKeyError:
                    vessels.photo = vessels.photo
                vessels.save()
            else:
                vessels.name = name_ship
                vessels.IMO = 0
                vessels.type = new_type
                vessels.user = new_user
                vessels.save()
            return HttpResponseRedirect('/Administrator/')
        if 'close' in request.POST:
            return HttpResponseRedirect('/Administrator/')
    return render(request, 'user/change_vessels.html', context={'change': change_change, 'user_name': user_name,
                                                                'all_type': all_type, 'all_users': all_users})


def change_vessels_creator(request, id):
    change_change = Vessels.objects.filter(id=id)
    login = request.session['login']
    user_name = Person.objects.filter(login=login)
    all_type = Type.objects.all().values()
    all_users = Person.objects.all()
    if request.method == 'POST':
        if 'changeButton' in request.POST:
            name_ship = request.POST.get('name_change_ship')
            IMO_ship = request.POST.get('IMO_change_ship')
            type_ship = request.POST.get('type_change_ship')
            user_ship = request.POST.get('user_change_ship')
            new_type = Type.objects.get(type=type_ship)
            new_user = Person.objects.get(name=user_ship)
            vessels = Vessels.objects.get(id=id)
            if IMO_ship != '':
                vessels.name = name_ship
                vessels.IMO = IMO_ship
                vessels.type = new_type
                vessels.user = new_user
                try:
                    photo = request.FILES['photo']
                    vessels.photo = photo
                except MultiValueDictKeyError:
                    vessels.photo = vessels.photo
                vessels.save()
            else:
                vessels.name = name_ship
                vessels.IMO = 0
                vessels.type = new_type
                vessels.user = new_user
                try:
                    photo = request.FILES['photo']
                    vessels.photo = photo
                except MultiValueDictKeyError:
                    vessels.photo = vessels.photo
                vessels.save()
            return HttpResponseRedirect('/creator/vessels/')
        if 'close' in request.POST:
            return HttpResponseRedirect('/creator/vessels/')
    return render(request, 'user/change_vessels.html', context={'change': change_change, 'user_name': user_name,
                                                                'all_type': all_type, 'all_users': all_users})


def change_user_creator(request, id):
    change_change = Person.objects.filter(id=id)
    login = request.session['login']
    user_name = Person.objects.filter(login=login)
    if request.method == 'POST':
        if 'changeButton' in request.POST:
            person = Person.objects.get(id=id)
            person.first_name = request.POST.get('first_name_change_person')
            person.second_name = request.POST.get('secondname_change_person')
            person.name = person.first_name + ' ' + person.second_name
            person.type = request.POST.get('type_change_person')
            new_password = request.POST.get('result')
            if new_password != '':
                h_pass = hashlib.md5(new_password.encode())
                new_password = h_pass.hexdigest()
                person.password = new_password
            person.save()
            return HttpResponseRedirect('/creator/users/')
        if 'close' in request.POST:
            return HttpResponseRedirect('/creator/users/')
    return render(request, 'user/change_user_creator.html', context={'change': change_change, 'user_name': user_name})


def fuel(request, id):
    login = request.session['login']
    user_name = Person.objects.filter(login=login)
    fuel_constant = Fuel.objects.filter(vessels_id=id)
    if request.method == 'POST':
        if 'save_change' in request.POST:
            fuel = Fuel.objects.get(vessels_id=id)
            fuel.b_r = request.POST.get('b_r')
            fuel.b_b = request.POST.get('b_b')
            fuel.b_c = request.POST.get('b_c')
            fuel.N = request.POST.get('N')
            fuel.Q = request.POST.get('Q')
            fuel.V = request.POST.get('V')
            fuel.C = request.POST.get('C')
            fuel.K = request.POST.get('K')
            fuel.X = request.POST.get('X')
            fuel.E = request.POST.get('E')
            fuel.save()
    return render(request, 'user/fuel.html', context={'person': user_name, 'fuel_constant': fuel_constant})


def show_on_map(request, id, IMO, name):
    from bs4 import BeautifulSoup
    import requests
    url = "https://www.marinetraffic.com/en/ais/details/ships/imo:{}/vessel:{}".format(IMO, name)
    headers = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate",
        "user-agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    coord = soup.find('link')
    l = str(coord)
    j, j1 = 0, 0
    id_id = ''
    for i in range(len(l) - 1):
        if l[i] == '/' and l[i + 1] == '/':
            j = i + 1
    for i1 in range(j, len(l) - 1):
        if l[i1] == 'i' and l[i1 + 1] == 'd':
            j1 = i1 + 3
    while l[j1] != '/':
        id_id += l[j1]
        j1 += 1
    url = "https://www.marinetraffic.com/vesselDetails/latestPosition/shipid:{}".format(id_id)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    vessels = Vessels.objects.get(id=id)
    vessels.latitude = data["lat"]
    vessels.longitude = data["lon"]
    speed = data["speed"]
    arrivalPort = data['arrivalPort']['name']
    status = data["shipStatus"]
    coord = Vessels.objects.filter(id=id)
    login = request.session['login']
    user_name = Person.objects.filter(login=login)
    url = "https://www.marinetraffic.com/en/vesselDetails/vesselInfo/shipid:{}".format(id_id)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    type = str(data["type"])
    icon = ''
    if type.startswith("Cargo"):
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/зеленый.png'
        else:
            vessels.icon = 'img/icons/на якоре зеленый.png'
    elif type == 'Tanker':
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/краснsй.png'
        else:
            vessels.icon = 'img/icons/на якоре красный.png'
    elif type == 'Passenger':
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/синий.png'
        else:
            vessels.icon = 'img/icons/на якоре синий.png'
    elif type == 'High Speed Craft':
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/желтый.png'
        else:
            vessels.icon = 'img/icons/на якоре желтый.png'
    elif type == 'Dive Vessel':
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/голубой.png'
        else:
            vessels.icon = 'img/icons/на якоре голубой.png'
    elif type == 'Fishing':
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/оранжевый.png'
        else:
            vessels.icon = 'img/icons/на якоре оранжевый.png'
    elif type == 'Unspecified':
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/серый.png'
        else:
            vessels.icon = 'img/icons/на якоре серый.png'
    else:
        if status == 'Underway using Engine':
            vessels.icon = 'img/icons/розовый.png'
        else:
            vessels.icon = 'img/icons/на якоре розовый.png'

    vessels.save()
    coord = Vessels.objects.filter(id=id)
    return render(request, 'user/on_map.html', context={'person': user_name, 'coord': coord, 'icon': icon,
                                                        'port': arrivalPort, 'speed': speed})
