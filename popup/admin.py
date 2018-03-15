# coding: utf-8
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ConfigContactForm , Contact , ConfigRegistrationForm , RegisterCourse, \
					PopUpThanksConsulting, PopUpThanksRegister, PopUpErrorRegister ,\
				    PopUpThanksEventRegister 
# Register your models here.
admin.site.register(ConfigContactForm, SingletonModelAdmin)
admin.site.register(ConfigRegistrationForm, SingletonModelAdmin)
admin.site.register(PopUpThanksConsulting, SingletonModelAdmin)
admin.site.register(PopUpThanksRegister, SingletonModelAdmin)
admin.site.register(PopUpErrorRegister , SingletonModelAdmin)
admin.site.register(PopUpThanksEventRegister , SingletonModelAdmin)

class ContactFormAdmin(admin.ModelAdmin):
	list_display  = [field.name  for field in Contact._meta.fields]

	class Meta:
		model = Contact

class RegisterCourseAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RegisterCourse._meta.fields]

	class Meta:
		model = RegisterCourse
			

admin.site.register(Contact , ContactFormAdmin)
admin.site.register(RegisterCourse , RegisterCourseAdmin)

