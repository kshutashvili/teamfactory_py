# Generated by Django 2.0 on 2018-02-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Site Name', max_length=255)),
                ('surname', models.CharField(default='Site Name', max_length=255)),
            ],
        ),
    ]
