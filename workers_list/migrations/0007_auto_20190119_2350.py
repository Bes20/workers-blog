# Generated by Django 2.1.1 on 2019-01-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers_list', '0006_auto_20190119_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workers',
            name='image',
            field=models.ImageField(default='workers_list/photos/default_user.jpg', upload_to='workers_list/photos', verbose_name='Фото сотрудника'),
        ),
    ]