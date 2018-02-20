# Generated by Django 2.0 on 2018-02-17 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0005_auto_20180217_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Курс который хотите посетить'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Введите вашу почту'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Введите ваше имя'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Введите ваш телефон'),
        ),
    ]