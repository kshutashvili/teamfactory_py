# Generated by Django 2.0 on 2018-02-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyWe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image', verbose_name='Рисунок в пиктограмме')),
                ('text', models.CharField(max_length=50, verbose_name='Текст пиктограммы')),
            ],
            options={
                'verbose_name': 'Пиктограммы блока "почему мы"',
            },
        ),
    ]
