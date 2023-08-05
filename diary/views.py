from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Notedata
from django.contrib.auth.decorators import login_required 
from .form import NoteForm
# Create your views here.

@login_required(login_url='signin')  
def Note(request):
    if request.user.is_superuser:
       data=Notedata.objects.order_by('dates')
       return render(request,'diary/Note.html',{'data':data})
    else:
        return HttpResponse("<h1>result not found</h1>")

@login_required(login_url='signin') 
def create_Note(request):
    if request.user.is_superuser:
       form=NoteForm()
       if request.method=='POST':
           form=NoteForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('Note')
   
       context={'form':form}
       return render(request,'diary/create_update.html',context)
    else:
        return HttpResponse("<h1>result not found</h1>")

@login_required(login_url='signin') 
def update_Note(request,pk):
    if request.user.is_superuser:
       orders=Notedata.objects.get(id=pk)
       form=NoteForm(instance=orders)
       if request.method=='POST':
           form=NoteForm(request.POST,instance=orders)
           if form.is_valid():
               form.save()
               return redirect('Note')
       context={'form':form}
       return render(request,'diary/create_update.html',context)
    else:
        return HttpResponse("<h1>result not found</h1>")

@login_required(login_url='signin') 
def delete_Note(request,pk):
    if request.user.is_superuser:
       orders=Notedata.objects.get(id=pk)
       if request.method=='POST':
           orders.delete()
           return redirect('Note')
       context={'item':orders}
       return render(request,'diary/delete.html',context)
    else:
        return HttpResponse("<h1>result not found</h1>")