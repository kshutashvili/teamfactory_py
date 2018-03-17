# coding: utf-8
from django.db import models
from django.contrib.postgres.fields import JSONField
from solo.models import SingletonModel
from django.utils.translation import ugettext as _
# Create your models here.


class Lector(models.Model):
	name = models.CharField(max_length=50  , verbose_name='Имя лектора')
	surname = models.CharField(max_length=50  , verbose_name='Фамилия лектора')
	position  = models.CharField(max_length=200 ,verbose_name='Должность лектора')

	def __str__(self):
		return "{0} {1}".format(self.name , self.surname)

	class Meta:
		verbose_name = 'Лектор'
		verbose_name_plural = 'Лекторы'



class Event(models.Model):
	lector = models.ForeignKey(Lector , verbose_name='лектор' , on_delete=models.CASCADE)
	theme  = models.CharField(max_length=500 , verbose_name="Тема лекции")
	where  = models.CharField(max_length=100 , verbose_name='Где' ,default='г.Киев ул. Соломенская 3')
	when   = models.DateTimeField(auto_now_add=False , auto_now= False ,verbose_name='Дата и время проведения')
	description  = models.TextField(max_length=3000 , verbose_name='Текст ивента')
	pub_date  = models.DateField(auto_now=True , verbose_name='Дата создания')
	def __str__(self):
		return 'Лектор - {0} , Тема - {1} , Когда - {2}'.format(self.lector.name , self.theme , self.when)

	class Meta:
		verbose_name = 'Ивент'
		verbose_name_plural = 'Ивенты'


class ConfigurationEventsPopUp(SingletonModel):
	text_where  = models.CharField(max_length=100 , verbose_name='Блок где' , default='Где')
	text_when  = models.CharField(max_length=100 , verbose_name='Блок Когда' , default='Когда')
	text_lector  = models.CharField(max_length=100 , verbose_name='Блок автора' , default='Автор')
	name_form = models.CharField(max_length=100 , verbose_name='Название формы')
	text_form = models.CharField(max_length=100 , verbose_name='Вспомогательный текст в форме')
	btn  = models.CharField(max_length=30 , verbose_name='Кнопка в форме')

	class Meta:
		verbose_name = "Настройка модального окна Ивента "

class RegisterEvent(models.Model):
	name_client  = models.CharField(max_length=50 , verbose_name=_('Имя'))
	phone_client  = models.CharField(max_length=50 , verbose_name=_('Номер телефона'))
	event  = models.ForeignKey(Event , on_delete=models.CASCADE , blank=True , null=True)

	class Meta:
		verbose_name = 'Регистрации на ивент'