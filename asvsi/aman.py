from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from dart.models import C_data,flutter_data,django_data,web3,solidity
from data_structure.models import data_structure

def home(request):
    context={
        "ds":data_structure.objects.all().count(),
        "c":C_data.objects.all().count(),
        "flutter":flutter_data.objects.all().count(),
        "django":django_data.objects.all().count(),
        "web3":web3.objects.all().count(),
        "solidity":solidity.objects.all().count(),
    }
    return render(request,'home.html',context=context)
    #return HttpResponse("hello")


def blog(request):
    return render(request,'blog.html')

def images(request):
    return render(request,'images.html')

#def flutter(request):
    return render(request,'flutter.html')


