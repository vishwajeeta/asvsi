from django.urls import path
from . import views

urlpatterns=[
    path('',views.Note,name='Note'),
    path('create_Note',views.create_Note,name='create_Note'),
    path('update_Note/<str:pk>/',views.update_Note,name='update_Note'),
    path('delete_Note/<str:pk>/',views.delete_Note,name='delete_Note')
]