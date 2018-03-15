# coding: utf-8
from django.contrib import admin 
from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import MainView , RegistrationCourse
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    # path('', MainView.as_view()  , name = 'static_pages'),
    # path('/registration-course/', RegistrationCourse.as_view() , name = 'registration-course'),
    # re_path('^detail-event/$', RegistrationCourse.as_view() , name = 'registration-course'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)