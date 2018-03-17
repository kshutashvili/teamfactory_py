# coding: utf-8
from django.contrib import admin 
from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name  = 'event'


urlpatterns = [
    path('<int:pk>/', views.EventJSON.as_view() ,  name= 'detail-event'),
    # path('', views.test ,  name= 'register-event'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)