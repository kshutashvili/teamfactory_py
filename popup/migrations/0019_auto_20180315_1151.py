# Generated by Django 2.0.2 on 2018-03-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0018_auto_20180315_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='popupthanksconsulting',
            name='text_ru',
            field=models.TextField(max_length=1000, null=True, verbose_name='Текст "Окно после заказа консультации"'),
        ),
        migrations.AddField(
            model_name='popupthanksconsulting',
            name='text_ua',
            field=models.TextField(max_length=1000, null=True, verbose_name='Текст "Окно после заказа консультации"'),
        ),
    ]
