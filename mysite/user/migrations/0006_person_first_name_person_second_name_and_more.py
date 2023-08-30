# Generated by Django 4.0.3 on 2022-05-12 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_person_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default=models.CharField(max_length=300), max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='second_name',
            field=models.CharField(default=models.CharField(max_length=300), max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(default='img/users/default.jpg', upload_to='img/users'),
        ),
        migrations.AlterField(
            model_name='vessels',
            name='photo',
            field=models.ImageField(default='img/ship/no-image.jpg', upload_to='img/ship'),
        ),
    ]