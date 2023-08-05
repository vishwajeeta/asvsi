from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='flutter'),
    path('flutter/<str:name>/<int:id>',views.flutter,name='flutter_page'),

    path('c',views.home_c,name='c'),
    path('c/<str:name>/<int:id>',views.c,name='c_page'),

    path('django',views.djangehome,name='django'),
    path('django/<str:name>/<int:id>',views.django,name='djangohome'),

    path('web3',views.web3home,name='web3'),
    path('web3/<str:name>/<int:id>',views.web_3,name='web3home'),

    path('solidity',views.solidityhome,name='solidity'),
    path('solidity/<str:name>/<int:id>',views.solidity_,name='solidityhome'),


    #dart
    path('python',views.python,name='python'),
    path('website',views.website,name='website'),
    path('blockchain',views.blockchain,name='blockchain'),
]