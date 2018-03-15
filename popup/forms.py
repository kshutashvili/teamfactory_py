# coding: utf-8
from django.forms import ModelForm
from popup.models import Contact , RegisterCourse
from django.forms.widgets import Media, MediaDefiningClass, Textarea, TextInput
from django.utils.translation import ugettext_lazy as _
class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'mail', 'contact_phone', 'course']
		widgets = {
            'name': TextInput(attrs={'placeholder': _('Ваше имя')}),
            'mail': TextInput(attrs={'placeholder': 'example@example.com'}),
            'contact_phone': TextInput(attrs={'placeholder': 'Ваш номер'}),
        }


class RegisterCourseForm(ModelForm):
	class Meta:
		model = RegisterCourse
		fields = ['name' , 'phone' , 'course']
		widgets = {
            'name': TextInput(attrs={'placeholder': _('Ваше имя')}),
            'phone': TextInput(attrs={'placeholder': 'Ваш номер'}),
        }


