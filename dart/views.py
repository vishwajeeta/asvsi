from django.shortcuts import render
from .models import flutter_data,C_data,django_data,web3,solidity
from django.contrib.auth.decorators import login_required

#dart

# Create your views here.
@login_required(login_url='signin')  
def website(request):
    return render(request,'website.html')

@login_required(login_url='signin')  
def python(request):
    return render(request,'python.html')

@login_required(login_url='signin')  
def blockchain(request):
    return render(request,'blockchain.html')



# Create your views here.
def home(request):
    data=flutter_data.objects.order_by('App_Name')
    return render(request,'dart/flutter_home.html',{'data':data})

# flutter details
@login_required(login_url='signin')  
def flutter(request,name,id):
    a=flutter_data
    product=a.objects.get(id=id)
    return render(request,'dart/flutter.html',{'data':product})

#c-language
@login_required(login_url='signin')  
def home_c(request):
    data=C_data.objects.order_by('App_Name')
    return render(request,'dart/c_home.html',{'data':data})

# flutter details
@login_required(login_url='signin')  
def c(request,name,id):
    product=C_data.objects.get(id=id)
    return render(request,'dart/c.html',{'data':product})

#single page
@login_required(login_url='signin')  
def django(request,name,id):
    product=django_data.objects.get(id=id)
    return render(request,'dart/django.html',{'data':product})

#single page
@login_required(login_url='signin')  
def djangehome(request):
    data=django_data.objects.order_by('App_Name')
    return render(request,'dart/djangohome.html',{'data':data})


#single page
@login_required(login_url='signin')  
def web_3(request,name,id):
    product=web3.objects.get(id=id)
    return render(request,'dart/web3.html',{'data':product})

#single page
@login_required(login_url='signin')  
def web3home(request):
    data=web3.objects.order_by('App_Name')
    return render(request,'dart/web3_home.html',{'data':data})


#single page
@login_required(login_url='signin')  
def solidity_(request,name,id):
    product=solidity.objects.get(id=id)
    return render(request,'dart/solidity.html',{'data':product})

#single page
@login_required(login_url='signin')  
def solidityhome(request):
    data=solidity.objects.order_by('App_Name')
    return render(request,'dart/solidity_home.html',{'data':data})