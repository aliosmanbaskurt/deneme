from django.shortcuts import render,redirect
from pages.models import Future
from django.contrib.auth.models import User
from memories.models import Memory,Category,Tag
import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import LoginForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def index (request):
    histories= Memory.objects.all().filter(date__month = datetime.datetime.now().month, date__day=datetime.datetime.now().day).order_by('?')[:1]
    
    context = {
        
        'histories' : histories
    }
    return render (request,'index.html',context)
    
@login_required(login_url='login')
def future (request):
    futures=Future.objects.all().order_by('future_date')
    context={
        'futures': futures
    }
    return render(request, 'future.html',context)

@login_required(login_url='login')
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

def user_login (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Aktif Olmayan Kullanıcı')
            else:
                messages.info(request, 'Geçersiz Kullanıcı')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')