from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Event , RegisterEvent
from django.http import JsonResponse
from json_views.views import JSONDetailView
from .forms import EventForm
import json
from django.core import serializers
from django.core.mail import send_mail , BadHeaderError
from django.conf import settings
# from django.views.generic.detail import BaseDetailView
# Create your views here.


# class EventDetailView(DetailView):

#     model = Event
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
# def test(request , id):
#   print(id)
#   return HttpResponse(id)

class EventJSON(JSONDetailView):
    model = Event


def test(request):
	if request.method == "POST":
		if request.is_ajax():
			name = request.POST['name']
			phone = request.POST['phone']
			event_id = request.POST['id_event']
			event_theme = Event.objects.get(id=event_id).theme
			RegisterEvent.objects.create(name_client=name,phone_client=phone,event_id=event_id)
			context = {
				'ok': 'OK!'
			}
			msg = 'Имя клиента :' + name + " "
			msg += 'Телефон  клиента :' + phone + " "
			msg += ' Ивент:' + event_theme + " "
			try:
				send_mail("Регистрация на ивент", msg, settings.EMAIL_HOST_USER ,  [settings.EMAIL_HOST_USER])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')

			# context_json = serializers.serialize('json', context)
			
			return JsonResponse(context)

