from django.urls import path
from . import views

urlpatterns=[
    path('',views.web_apps,name='web_apps'),
    
]
