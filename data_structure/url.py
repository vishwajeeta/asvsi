from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="data_structure"),
    path('ds_search',views.search,name="ds_search")
]