from django.contrib import admin
from .models import Lector , Event , ConfigurationEventsPopUp , RegisterEvent
from solo.admin import SingletonModelAdmin
# Register your models here.



class LectorAdmin(admin.ModelAdmin):
	list_display  = [field.name  for field in Lector._meta.fields]

	class Meta:
		model = Lector

class RegisterEventAdmin(admin.ModelAdmin):
	list_display = [field.name for field in RegisterEvent._meta.fields]

	class Meta:
		model = RegisterEvent

class EventAdmin(admin.ModelAdmin):
	list_display = ['id' , 'lector' , 'theme' , 'when']

	class Meta:
		model = Event

admin.site.register(Lector , LectorAdmin)
admin.site.register(Event , EventAdmin)
admin.site.register(RegisterEvent , RegisterEventAdmin)
admin.site.register(ConfigurationEventsPopUp , SingletonModelAdmin)



