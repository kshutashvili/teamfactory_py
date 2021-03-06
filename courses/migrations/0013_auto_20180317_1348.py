# Generated by Django 2.0.2 on 2018-03-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20180315_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='position',
            field=models.CharField(max_length=300, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='author',
            name='position_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='author',
            name='position_ua',
            field=models.CharField(max_length=300, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=3000, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_ru',
            field=models.TextField(max_length=3000, null=True, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description_ua',
            field=models.TextField(max_length=3000, null=True, verbose_name='Описание курса'),
        ),
    ]
