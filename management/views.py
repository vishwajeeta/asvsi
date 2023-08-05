from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect
from .models import Profile
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'User alrady exist')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #log user in and reditrcet to setting page

                #create a profile object for new user
                user_model=User.objects.get(username=username)
                new_profile=Profile.objects.create(user=user_model,id_user=user_model.id)
                new_profile.save()
                return redirect('signin')

        else:
            messages.info(request,'password not matching')
            return redirect('signup')
            
    else:
        
       return render(request,'management/signup.html')

def signin(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            
            return redirect('/')
        else:
            messages.info(request,'invallid crediencial')
            return redirect('signin')
        
    else:
        
        return render(request,'management/signin.html')

#logout
@login_required(login_url='signin')  
def logout(request):
    auth.logout(request)
    return redirect('signin')