from django.shortcuts import render ,redirect
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Test  , SiteConfiguration , Header , WhyWe
from courses.models import Author , Course 
from popup.models import RegisterCourse
from django.views.generic import TemplateView
from popup.forms import ContactForm , RegisterCourseForm
from django.core.mail import send_mail , BadHeaderError
from django.conf import settings
from django.http import JsonResponse
import json


class MainView(TemplateView):

	def get_ctx(self):
		form  = ContactForm()
		form_course  = RegisterCourseForm()
		why_we  = WhyWe.objects.all()
		authors_all = Author.objects.all()
		courses_all = Course.objects.all()

		context  = {
		'why_we': why_we,
		'courses_all': courses_all,
		'form': form,
		'form_course': form_course,
		}
		return context

	def get(self , request):
		return render(request , 'main.html' , self.get_ctx())

	def post(self , request):
		form  = ContactForm(request.POST)
		ctx = {}
		if form.is_valid():
			data = form.cleaned_data
			name_course = Course.objects.get(id=data['course'].id).name_ru
			mail = data['mail']
			msg  = "Имя : " + data['name'] + ' '
			msg  += " Телефон " + data['contact_phone'] + ' '
			msg  += " Почта " + data['mail'] + ' '
			msg  += " Интересуемый курс: " + name_course + ' '
			form.save()
			try:
				send_mail("Заявка на перезвон", msg, settings.EMAIL_HOST_USER ,  [settings.EMAIL_HOST_USER])
				ctx['result'] = 'thanks'
				for key in self.get_ctx():
					ctx[key] = self.get_ctx()[key]
			except BadHeaderError:
				return HttpResponse('Invalid header found.')

			return render(request , 'main.html' , ctx)
		else:
			form = ContactForm()
		return HttpResponse('asdasd')


class RegistrationCourse(TemplateView):

	def get(self, request):
		return HttpResponse('asdasd')

	def post(self , request):
		if request.is_ajax():
			print('AJAX!!!!')
			name = request.POST["name"]
			phone = request.POST["phone"]
			course_id = request.POST["course_id"]
			RegisterCourse.objects.create(name=name,
											 phone=phone, 
											 course=Course.objects.get(id=course_id)
											 )
			try:

				old_number_seats = Course.objects.get(id=course_id).number_of_seats
				new_number_seats  = old_number_seats  - 1
			except:
				context = {
				'test': 'test',
				'course_id': course_id
			}
			Course.objects.filter(id=course_id).update(number_of_seats=new_number_seats)
			message = 'Имя клиента -  '  + name + " ,"
			message += "Телефон -" + phone +  " ,"
			message += "Курс -" + Course.objects.get(id=course_id).name_ru
			context = {
				'new_number_seats': new_number_seats ,
				'course_id': course_id
			}
			try:
				send_mail("Запись на курс ", message, settings.EMAIL_HOST_USER ,  [settings.EMAIL_HOST_USER])
				
			except BadHeaderError:
				return HttpResponse('Invalid header found.')

			return HttpResponse(json.dumps(context))
