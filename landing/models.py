from django.db import models

# Create your models here.

from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    icon  = models.ImageField(blank= True , null=True , verbose_name = 'Иконка' , upload_to='image')
    
    def __str__(self):
        return "Название сайта(title)"

    class Meta:
        verbose_name = "Название сайта(title)"


class Header(SingletonModel):
	image  = models.ImageField(blank= True , null=True , verbose_name = 'Фоновый рисунок в хедере' , upload_to='image')
	header_text  = models.TextField(max_length= 1000 , verbose_name = 'Текст в хедере')
	btn_learn = models.CharField(max_length=50, verbose_name = 'Кнопка учиться')
	btn_presentation = models.CharField(max_length=50 ,verbose_name = 'Кнопка презентация' )
	link_presentation = models.CharField(max_length=300 , blank=True , null=True ,verbose_name = 'Ccылка на презентацию')

	def __str__(self):
		return self.header_text

	class Meta:
		verbose_name = 'Конфигурация хедера'


class Test(models.Model):
	name = models.CharField(max_length=255, default='Site Name')
	surname = models.CharField(max_length=255, default='Site Name')


class WhyWe(models.Model):
	image  = models.ImageField(blank= True , null=True , verbose_name = 'Рисунок в пиктограмме' , upload_to='image')
	text   = models.CharField(max_length = 50 , verbose_name = 'Текст пиктограммы')

	def __str__(self):
		return self.text

	class Meta:
		verbose_name = 'Пиктограмма блока "почему мы"'
		verbose_name_plural  = 'Пиктограммы блока "почему мы"'

class TextWhyWe(SingletonModel):
	text = models.TextField(max_length = 500 , verbose_name = 'Дополнительный текст для блока "почему мы"')

	class Meta:
		verbose_name = 'Дополнительный текст для блока почему мы'
