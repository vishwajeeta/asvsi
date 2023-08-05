from django.shortcuts import render
from .models import web_app
# Create your views here.

def web_apps(request):
    data=web_app.objects.order_by('App_Name')
    return render(request,'web_apps.html',{'data':data})