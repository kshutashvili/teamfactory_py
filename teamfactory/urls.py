"""teamfactory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from landing.views import MainView , RegistrationCourse 
from event.views import test

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', MainView.as_view() , name = 'static_page'),
    path('detail-event/', include('event.urls')),
    path('register-event/', test , name = 'register-event'),
    path('registration-course/', RegistrationCourse.as_view() , name = 'registration-course'),
    # path('check-email/', check_email , name = 'registration-course'),
    # path('<str:page_url>/', content.pages, name='static_pages'),
) 
 # path('', views.test ,  name= 'register-event'),
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         path('rosetta/', include('rosetta.urls'))
#     ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)