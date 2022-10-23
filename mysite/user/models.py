from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100, default=name)
    second_name = models.CharField(max_length=100, default=name)
    photo = models.ImageField(default='img/users/default.jpg', upload_to='img/users')
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=50)


    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class Type(models.Model):
    type = models.CharField(max_length=50)


class Vessels(models.Model):
    user = models.ForeignKey(Person, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    photo = models.ImageField(default='img/ship/no-image.jpg', upload_to='img/ship')
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    IMO = models.IntegerField()
    name_in_en = models.CharField(max_length=300, default=name)
    latitude = models.CharField(max_length=100, default='0')
    longitude = models.CharField(max_length=100, default='0')
    icon = models.ImageField(default='img/icons/краснsй.png', upload_to='img/icons')


class Fuel(models.Model):
    vessels = models.OneToOneField(Vessels, on_delete=models.CASCADE, primary_key=True)
    b_r = models.CharField(max_length=50)
    b_b = models.CharField(max_length=50)
    b_c = models.CharField(max_length=50)
    N = models.CharField(max_length=50)
    Q = models.CharField(max_length=50)
    V = models.CharField(max_length=50)
    C = models.CharField(max_length=50)
    K = models.CharField(max_length=50)
    X = models.CharField(max_length=50)
    E = models.CharField(max_length=50)
