from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def login(request):

 response_data = {}

 if request.method == "GET" :
        return render(request, 'login.html')

 elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)
        
        if not (login_username and login_password):
                 response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            try:
                myuser = User.objects.get(username=login_username) 
            
            
                if check_password(login_password, myuser.password):
                    request.session['user'] = myuser.id 
                    return redirect('/app')
                else:
                    response_data['error'] = "비밀번호를 틀렸습니다."
            except:
                    response_data['error'] = "없는 아이디 입니다."

        return render(request, 'login.html',response_data)
