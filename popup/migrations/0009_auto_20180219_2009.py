# Generated by Django 2.0 on 2018-02-19 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0008_registercourse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='contact_phone',
        ),
    ]
