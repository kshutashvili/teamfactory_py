# Generated by Django 2.0 on 2018-02-20 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20180219_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_of_seats',
            field=models.IntegerField(default=50, verbose_name='Количество мест на курс'),
        ),
    ]
