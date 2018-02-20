from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import ConfigContactForm , Contact , ConfigRegistrationForm , RegisterCourse
# Register your models here.
admin.site.register(ConfigContactForm, SingletonModelAdmin)
admin.site.register(ConfigRegistrationForm, SingletonModelAdmin)


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
