# Generated by Django 2.0 on 2018-02-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180216_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number_of_seats',
            field=models.PositiveIntegerField(default=50, verbose_name='Количество мест на курс'),
        ),
    ]
