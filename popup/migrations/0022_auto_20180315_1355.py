# Generated by Django 2.0.2 on 2018-03-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0021_auto_20180315_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='popupthanksregister',
            name='text_ru',
            field=models.TextField(max_length=1000, null=True, verbose_name='Текст "Окно после регистрации"'),
        ),
        migrations.AddField(
            model_name='popupthanksregister',
            name='text_ua',
            field=models.TextField(max_length=1000, null=True, verbose_name='Текст "Окно после регистрации"'),
        ),
    ]
