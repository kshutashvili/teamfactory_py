from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Event , RegisterEvent
from django.http import JsonResponse
from json_views.views import JSONDetailView
from .forms import EventForm

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
			# print(name)
			# print(phone)
			# print(event_id)
			RegisterEvent.objects.create(name_client=name,phone_client=phone,event_id=event_id)
			print('ok!')
			# print(requestphone)
	return HttpResponse("request")

