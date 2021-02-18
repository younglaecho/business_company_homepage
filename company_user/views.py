from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password 
# make_password : 비밀번호를 암호화     check_password : 비밀번호를 확인
from .models import Comuser
from .forms import LoginForm
# Create your views here.


def home(request):
    user_id = request.session.get('user')  # 세션으로부터 가져옴.

    if user_id:
        comuser = Comuser.objects.get(pk=user_id) # user_id를 기본키로 함


    return render(request, 'index.html')
    #     return HttpResponse(deathuser.username)

    # return HttpResponse('Home')

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

