from django.contrib import admin
from solo.admin import SingletonModelAdmin
from landing.models import SiteConfiguration
from landing.models import Test ,Header , WhyWe , TextWhyWe ,\
								 BlockForStudents ,Partners , ConfigFooter


admin.site.register(Test)
admin.site.register(WhyWe)
admin.site.register(Partners)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Header, SingletonModelAdmin)
admin.site.register(TextWhyWe, SingletonModelAdmin)
admin.site.register(BlockForStudents, SingletonModelAdmin)
admin.site.register(ConfigFooter, SingletonModelAdmin)