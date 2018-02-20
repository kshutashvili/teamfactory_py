from django.db import models
from solo.models import SingletonModel
from courses.models import Course
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
	name  = models.CharField(max_length=200 , verbose_name="Введите ваше имя" ,  blank= True)
	mail  = models.EmailField(max_length=254 , verbose_name="Введите вашу почту" , blank= True)
	contact_phone = models.CharField(max_length=35 , verbose_name="Введите ваш телефон" , blank= True)
	course = models.ForeignKey(Course , on_delete=models.CASCADE , verbose_name='Курс который хотите посетить')

	def __str__(self):
		return "Номер заказа - {0} , имя клиента - {1} , курс - {2}".format(self.id  , self.name , self.course.id)


class RegisterCourse(models.Model):
	name = models.CharField(max_length=50 , verbose_name='Ваше имя')
	phone  = models.CharField(max_length = 50 , verbose_name = 'Телефонный номер')
	course  = models.ForeignKey(Course , on_delete=models.CASCADE , verbose_name='Курс')


	def __str__(self):
		return "Номер заказа - {0} , имя клиента - {1} , курс - {2}".format(self.id  , self.name , self.course.id)

	class Meta:
		verbose_name = 'Регистрация на курсе'
		verbose_name_plural = 'Регистрации на курс'