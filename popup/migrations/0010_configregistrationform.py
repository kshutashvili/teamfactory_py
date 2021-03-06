# Generated by Django 2.0 on 2018-02-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popup', '0009_auto_20180219_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigRegistrationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='Заказать консультацию', max_length=50, verbose_name='Заголовок модального окна')),
                ('text', models.TextField(max_length=200, verbose_name='Вспомогательный текст')),
                ('button', models.CharField(max_length=50, verbose_name='Кнопка отправки')),
            ],
            options={
                'verbose_name': 'Настройка модального окна записи на курс',
            },
        ),
    ]
