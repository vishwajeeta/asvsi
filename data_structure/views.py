from django.shortcuts import render
from .models import data_structure
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    scroll=data_structure.objects.order_by('ranking')
    p=Paginator(data_structure.objects.order_by('ranking'),1)
    page=request.GET.get('page')
    data=p.get_page(page)
    return render(request,'data_structure/index.html',{"data":data,"scroll":scroll})
def search(request):
    if request.method=='POST':
        search=request.POST['search']
        data=data_structure.objects.filter(name=search)

    return render(request,'data_structure/search.html',{"data":data})