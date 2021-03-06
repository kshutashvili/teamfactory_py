# Generated by Django 2.0 on 2018-02-27 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20180222_1337'),
        ('landing', '0013_auto_20180227_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularСourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Первый популярный')),
            ],
            options={
                'verbose_name': 'Популярные курсы',
            },
        ),
    ]
