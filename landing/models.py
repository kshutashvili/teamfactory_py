# coding: utf-8
from django.db import models

# Create your models here.

from django.db import models
from solo.models import SingletonModel

from courses.models import Course
from django.utils.translation import ugettext as _

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default=_('TeamFactory') , verbose_name='Имя сайта')
    icon  = models.ImageField(blank= True , null=True , verbose_name = _('Иконка' ), upload_to='image')
    
    def __str__(self):
        return "Название сайта(title)"

    class Meta:
        verbose_name = "Название сайта(title)"


class Header(SingletonModel):
	image  = models.ImageField(blank= True , null=True , verbose_name = 'Фоновый рисунок в хедере' , upload_to='image')
	header_text  = models.TextField(max_length= 3000 , verbose_name = 'Текст в хедере')
	btn_learn = models.CharField(max_length=50, verbose_name = 'Кнопка учиться')
	btn_presentation = models.CharField(max_length=50 ,verbose_name = 'Кнопка презентация' )
	link_presentation = models.CharField(max_length=1000 , blank=True , null=True ,verbose_name = 'Ccылка на презентацию')

	def __str__(self):
		return self.header_text

	class Meta:
		verbose_name = 'Конфигурация хедера'


class Test(models.Model):
	name = models.CharField(max_length=255, default='Site Name')
	surname = models.CharField(max_length=255, default='Site Name')


class WhyWe(models.Model):
	image  = models.ImageField(blank= True , null=True , verbose_name = 'Рисунок в пиктограмме' , upload_to='image')
	text   = models.CharField(max_length = 300 , verbose_name = 'Текст пиктограммы')

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Пиктограмма блока "почему мы"'
		verbose_name_plural  = 'Пиктограммы блока "почему мы"'

class TextWhyWe(SingletonModel):
	text = models.TextField(max_length = 3000 , verbose_name = 'Дополнительный текст для блока "почему мы"')

	class Meta:
		verbose_name = 'Дополнительный текст для блока почему мы'



class BlockForStudents(SingletonModel):
	text  = models.TextField(max_length=3000 , verbose_name='Текст для студентов')
	image = models.ImageField(upload_to='image', verbose_name='Картинка для студентов')

	class Meta:
		verbose_name= "Блок для студентов"


class Partners(models.Model):
	image = models.ImageField(upload_to='image', verbose_name='Лого партнеров')

	class Meta:
		verbose_name= "Лого партнера"
		verbose_name_plural = 'Лого партнеров'

class PopularСourses(SingletonModel):
	first_course  = models.CharField(max_length=50 , verbose_name="Первый популярный" , blank=True , null=True)
	two_course  = models.CharField(max_length=50 , verbose_name="Второй популярный" , blank=True , null=True)
	three_course  = models.CharField(max_length=50 , verbose_name="Третий популярный" , blank=True , null=True)
	four_course  = models.CharField(max_length=50 , verbose_name="Четвертый популярный" , blank=True , null=True)
	
	class Meta:
		verbose_name = 'Популярные курсы'


class ConfigFooter(SingletonModel):
	skype = models.CharField(max_length=30 , verbose_name='Наш скайп')
	mail = models.CharField(max_length=30 , verbose_name='Наш mail')
	first_phone = models.CharField(max_length=30 , verbose_name='Первый номер')
	second_phone = models.CharField(max_length=30 , verbose_name='Второй номер')
	copyright  = models.CharField(max_length=60 , verbose_name='Копирайт'  , default='All rights reserved.')

	class Meta:
		verbose_name = 'Настройки футера'