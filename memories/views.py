from django.shortcuts import render
from . models import Memory

# Create your views here.

def memo_list (request):
    memory=Memory.objects.all().order_by('date')
    context={
        'memory': memory
    }
    return render (request, 'memories2.html',context)