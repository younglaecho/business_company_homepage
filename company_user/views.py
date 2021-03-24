from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password 
# make_password : 비밀번호를 암호화     check_password : 비밀번호를 확인
from .models import Comuser
from .forms import LoginForm
# Create your views here.


def home(request):
    return render(request, 'index.html')

def introduction(request):
    return render(request, 'introduction.html')

def waytocome(request):
    return render(request, 'waytocome.html')
 
def businesCoast(request):
    return render(request, 'business_coast.html')
    
def businessHarbor(request):
    return render(request, 'business_harbor.html')

def businessMarEnv(request):
    return render(request, 'business_marenv.html')

def businessMarPhysics(request):
    return render(request, 'business_marphysics.html')

def businessGIS(request):
    return render(request, 'business_gis.html')


def qanda(request):
    return render(request, 'qanda.html')
    
def recruit(request):
    return render(request, 'recruit.html')
    
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


def login(request):
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.user_id
            # session_code
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

