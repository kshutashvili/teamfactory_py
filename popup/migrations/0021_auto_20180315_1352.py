# Generated by Django 2.0.2 on 2018-03-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0020_auto_20180315_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='popupthankseventregister',
            name='text_ru',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='popupthankseventregister',
            name='text_ua',
            field=models.TextField(max_length=600, null=True),
        ),
    ]