from django.contrib import admin 
from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import MainView , RegistrationCourse


urlpatterns = [
    re_path('^$', MainView.as_view()),
    re_path('^registration-course/$', RegistrationCourse.as_view() , name = 'registration-course'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)