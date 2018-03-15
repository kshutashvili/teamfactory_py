# coding: utf-8
from django.contrib import admin 
from solo.admin import SingletonModelAdmin
from landing.models import SiteConfiguration
from landing.models import Test ,Header , WhyWe , TextWhyWe ,\
								 BlockForStudents ,Partners , ConfigFooter , PopularСourses

class HeaderAdmin(admin.ModelAdmin):
	class Meta:
		model = Header
		exclude  = ('header_text' , 'btn_learn' , 'btn_presentation')

admin.site.register(Test)
admin.site.register(WhyWe)
admin.site.register(Partners)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Header, SingletonModelAdmin)

admin.site.register(TextWhyWe, SingletonModelAdmin)
admin.site.register(BlockForStudents, SingletonModelAdmin)
admin.site.register(ConfigFooter, SingletonModelAdmin)
admin.site.register(PopularСourses, SingletonModelAdmin)