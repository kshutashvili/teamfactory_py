# Generated by Django 2.0 on 2018-02-27 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_popularсourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularсourses',
            name='first_course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Первый популярный'),
        ),
    ]
