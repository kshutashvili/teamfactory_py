# coding: utf-8
from django.db import models
from solo.models import SingletonModel
from courses.models import Course
from django.core.validators import validate_email
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class ConfigContactForm(SingletonModel):
	header  = models.CharField(max_length=50, default="Заказать консультацию" , verbose_name='Заголовок модального окна')
	text  = models.TextField(max_length=200 , verbose_name="Вспомогательный текст")
	button  = models.CharField(max_length=50 , verbose_name='Кнопка отправки')

	class Meta:
		verbose_name = 'Настройка модального окна связи'

class ConfigRegistrationForm(SingletonModel):
	header  = models.CharField(max_length=50, default="Заказать консультацию" , verbose_name='Заголовок модального окна')
	text  = models.TextField(max_length=200 , verbose_name="Вспомогательный текст")
	button  = models.CharField(max_length=50 , verbose_name='Кнопка отправки')

	class Meta:
		verbose_name = 'Настройка модального окна записи на курс'



class Contact(models.Model):
	name  = models.CharField(max_length=200 , verbose_name=_("Введите ваше имя") ,  blank= True)
	mail  = models.EmailField(max_length=254 , verbose_name=_("Введите вашу почту") , blank= True , validators=[validate_email])
	contact_phone = models.CharField(max_length=35 , verbose_name=_("Введите ваш телефон") , blank= True)
	course = models.ForeignKey(Course , on_delete=models.CASCADE , verbose_name=_('Курс который хотите посетить'))

	def __str__(self):
		return "Номер заказа - {0} , имя клиента - {1} , курс - {2}".format(self.id  , self.name , self.course.id)

	class Meta:
		verbose_name = 'Запись на консультацию'
		verbose_name_plural = 'Записи на консультации'

class RegisterCourse(models.Model):
	name = models.CharField(max_length=50 , verbose_name='Ваше имя')
	phone  = models.CharField(max_length = 50 , verbose_name = 'Телефонный номер')
	course  = models.ForeignKey(Course , on_delete=models.CASCADE , verbose_name='Курс')


	def __str__(self):
		return "Номер заказа - {0} , имя клиента - {1} , курс - {2}".format(self.id  , self.name , self.course.id)

	class Meta:
		verbose_name = 'Регистрация на курсе'
		verbose_name_plural = 'Регистрации на курс'


class PopUpThanksConsulting(SingletonModel):
	text = models.TextField(max_length=1000 , verbose_name='Текст "Окно после заказа консультации"')

	class Meta:
		verbose_name = 'Текст "Окно после заказа консультации"'
	

class PopUpThanksRegister(SingletonModel):
	text = models.TextField(max_length=1000 , verbose_name='Текст "Окно после регистрации"')

	class Meta:
		verbose_name = 'Текст "Окно после заказа регистрации"'	

class PopUpErrorRegister(SingletonModel):
	text = models.TextField(max_length=1000 , verbose_name='Текст "Ошибка при регистрации"')

	class Meta:
		verbose_name = 'Текст "Ошибка при регистрации"'	


class PopUpThanksEventRegister(SingletonModel):
	text  = models.TextField(max_length=600)

	class Meta:
		verbose_name = 'Tекст модального окна "спасибо за регистрацию на ивент"'

