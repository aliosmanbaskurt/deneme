from django.shortcuts import render
from . models import Future
from memories.models import Memory,Category,Tag
import datetime
# Create your views here.


def index (request):
    histories= Memory.objects.all().filter(date__month = datetime.datetime.now().month, date__day=datetime.datetime.now().day).order_by('?')[:1]
    
    context = {
        
        'histories' : histories
    }
    return render (request,'index.html',context)

def future (request):
    futures=Future.objects.all().order_by('future_date')
    context={
        'futures': futures
    }
    return render(request, 'future.html',context)

def story (request):
    memory= Memory.objects.all().order_by('date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'memory':memory,
        'tags':tags,
        'categories': categories
    }
    return render (request, 'ourstory.html',context)

