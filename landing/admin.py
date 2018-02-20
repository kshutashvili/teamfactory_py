from django.contrib import admin

# Register your models here.
from solo.admin import SingletonModelAdmin
from landing.models import SiteConfiguration
from landing.models import Test ,Header , WhyWe , TextWhyWe 




admin.site.register(Test)
admin.site.register(WhyWe)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
admin.site.register(Header, SingletonModelAdmin)
admin.site.register(TextWhyWe, SingletonModelAdmin)

# There is only one item in the table, you can get it this way:
from .models import SiteConfiguration
# config = SiteConfiguration.objects.get()

# get_solo will create the item if it does not already exist
# config = SiteConfiguration.get_solo()