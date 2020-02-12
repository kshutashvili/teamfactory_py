# Generated by Django 2.0.2 on 2018-03-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0027_auto_20180316_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockforstudents',
            name='text',
            field=models.TextField(max_length=3000, verbose_name='Текст для студентов'),
        ),
        migrations.AlterField(
            model_name='blockforstudents',
            name='text_ru',
            field=models.TextField(max_length=3000, null=True, verbose_name='Текст для студентов'),
        ),
        migrations.AlterField(
            model_name='blockforstudents',
            name='text_ua',
            field=models.TextField(max_length=3000, null=True, verbose_name='Текст для студентов'),
        ),
        migrations.AlterField(
            model_name='header',
            name='header_text',
            field=models.TextField(max_length=3000, verbose_name='Текст в хедере'),
        ),
        migrations.AlterField(
            model_name='header',
            name='header_text_ru',
            field=models.TextField(max_length=3000, null=True, verbose_name='Текст в хедере'),
        ),
        migrations.AlterField(
            model_name='header',
            name='header_text_ua',
            field=models.TextField(max_length=3000, null=True, verbose_name='Текст в хедере'),
        ),
        migrations.AlterField(
            model_name='header',
            name='link_presentation',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ccылка на презентацию'),
        ),
        migrations.AlterField(
            model_name='textwhywe',
            name='text',
            field=models.TextField(max_length=3000, verbose_name='Дополнительный текст для блока "почему мы"'),
        ),
        migrations.AlterField(
            model_name='textwhywe',
            name='text_ru',
            field=models.TextField(max_length=3000, null=True, verbose_name='Дополнительный текст для блока "почему мы"'),
        ),
        migrations.AlterField(
            model_name='textwhywe',
            name='text_ua',
            field=models.TextField(max_length=3000, null=True, verbose_name='Дополнительный текст для блока "почему мы"'),
        ),
        migrations.AlterField(
            model_name='whywe',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Текст пиктограммы'),
        ),
        migrations.AlterField(
            model_name='whywe',
            name='text_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Текст пиктограммы'),
        ),
        migrations.AlterField(
            model_name='whywe',
            name='text_ua',
            field=models.CharField(max_length=300, null=True, verbose_name='Текст пиктограммы'),
        ),
    ]