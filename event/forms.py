from django import forms
from .models import RegisterEvent


class EventForm(forms.ModelForm):
	class Meta:
		model = RegisterEvent
		exclude  = ['id' , 'event']



