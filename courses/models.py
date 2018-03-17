# coding: utf-8
from django.db import models

# Create your models here.


class Author(models.Model):
	name  = models.CharField(max_length=50 , verbose_name= "Имя автора")
	surname  = models.CharField(max_length=50 , verbose_name= "Фамилия автора")
	image  = models.ImageField(blank= True , null=True , verbose_name = 'Фото автора' , upload_to='image')
	position  = models.CharField(max_length=300 , verbose_name= "Должность")

	def __str__(self):
		return self.name + ' ' + self.surname

	class Meta:
		verbose_name = 'Автор'
		verbose_name_plural  = 'Авторы'


class Course(models.Model):
	author = models.ForeignKey(Author , verbose_name='Выберите автора' , on_delete=models.CASCADE)
	name_ru  = models.CharField(max_length=100 , verbose_name='Название курса на русском')
	name_en  = models.CharField(max_length=100 , verbose_name='Название курса на английском')
	description  = models.TextField(max_length=3000 , verbose_name='Описание курса')
	duration  = models.CharField(max_length=50 , verbose_name='Длительность курса')
	start_course  = models.DateField(auto_now_add=False , auto_now= False, verbose_name='Старт курса')
	end_course  = models.DateField(auto_now_add=False , auto_now= False ,verbose_name='Конец курса')
	background  = models.ImageField(blank= True , null=True , verbose_name = 'Фоновая картинка' , upload_to='image')
	shedule_btn_text = models.CharField(default= 'Расписание' , max_length=100 , verbose_name=' Текст кнопки расписания')
	upload = models.FileField(upload_to='uploads/' , verbose_name='Припрепить файл с расаписанием')
	learn_btn_text = models.CharField(default= 'Записаться' ,max_length=100 , verbose_name='Текст кнопки учиться')
	number_of_seats  = models.PositiveIntegerField(default=50, verbose_name = 'Количество мест на курс')	

	def __str__(self):
		return self.name_ru


	class Meta:
		verbose_name = "Курс"
		verbose_name_plural = "Курсы"