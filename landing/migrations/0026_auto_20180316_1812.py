# Generated by Django 2.0.2 on 2018-03-16 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0025_auto_20180315_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockforstudents',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='blockforstudents',
            name='text_ua',
        ),
        migrations.RemoveField(
            model_name='configfooter',
            name='copyright_ru',
        ),
        migrations.RemoveField(
            model_name='configfooter',
            name='copyright_ua',
        ),
        migrations.RemoveField(
            model_name='header',
            name='btn_learn_ru',
        ),
        migrations.RemoveField(
            model_name='header',
            name='btn_learn_ua',
        ),
        migrations.RemoveField(
            model_name='header',
            name='btn_presentation_ru',
        ),
        migrations.RemoveField(
            model_name='header',
            name='btn_presentation_ua',
        ),
        migrations.RemoveField(
            model_name='header',
            name='header_text_ru',
        ),
        migrations.RemoveField(
            model_name='header',
            name='header_text_ua',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='first_course_ru',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='first_course_ua',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='four_course_ru',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='four_course_ua',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='three_course_ru',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='three_course_ua',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='two_course_ru',
        ),
        migrations.RemoveField(
            model_name='popularсourses',
            name='two_course_ua',
        ),
        migrations.RemoveField(
            model_name='textwhywe',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='textwhywe',
            name='text_ua',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='whywe',
            name='text_ua',
        ),
    ]
