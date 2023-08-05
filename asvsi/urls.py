"""asvsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
#import images
from django.conf import settings
from django.conf.urls.static import static
from . import aman

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',aman.home,name='home'),
    
    
    path('blog',aman.blog,name='blog'),
    
    
    path('images',aman.images,name='gallary'),
    path('flutter/',include('dart.url')),
    

    path('web_apps/',include('web.url')),
    path('account/',include('management.url')),
    path('diary/',include('diary.url')),
    path('data_sturcture',include('data_structure.url')),
    

    path('pdf/',include('pdf.url')),

    
]

urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)