"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='main'),
    path('user/', views.user, name='user'),
    path('exit/', views.exit, name='exit'),
    path('redact/', views.change, name='change'),
    path('fuel/<int:id>/', views.fuel, name='fuel'),
    path('map/<int:id>/<int:IMO>/<str:name>/', views.show_on_map),
    path('Administrator/', views.admin, name='admin'),
    path('Administrator/delete_vessels/<int:id>/', views.delete_vesselse),
    path('Administrator/show_vessels/<int:id>/', views.show_person_vessels),
    path('Administrator/change_vessels/<int:id>/', views.change_vessels),
    path('creator/', views.creator_example),
    path('creator/vessels/', views.creator_vessels, name='creator_vessels'),
    path('creator/users/', views.creator_users, name='creator_users'),
    path('creator/vessels/delete_vessels/<int:id>/', views.delete_vesselse_creator),
    path('creator/vessels/show_vessels/<int:id>/', views.show_person_vessels),
    path('creator/users/delete_user/<int:id>/', views.delete_user_creator),
    path('creator/vessels/change_vessels/<int:id>/', views.change_vessels_creator),
    path('creator/users/change_user/<int:id>/', views.change_user_creator),
    ]
