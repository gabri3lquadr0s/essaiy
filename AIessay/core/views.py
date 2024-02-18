from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as Login_process, logout as Logout_process
from . forms import CreateUser, ChangeUser, AuthUser
from django.contrib.auth.decorators import login_required

def login(request):
    loginForm = AuthUser()
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('dashboard')
        else:
            return redirect('index')
    else:
        if 'username' in request.POST:
            loginForm = AuthUser(request, data=request.POST)
            if loginForm.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    Login_process(request, user)
                    if user.is_staff:
                        return redirect('dashboard')
                    else:
                        return redirect('index')
                else:
                    return render(request, 'core/login.html', {'err':'User does not exist', 'loginForm': loginForm})
            else:
                return render(request, 'core/login.html', {'err':'Error authenticating, please check your data', 'loginForm': loginForm})
        
    return render(request, 'core/login.html', {'loginForm': loginForm})

def logout(request):
    Logout_process(request)
    return redirect('login')

def create(request):
    createForm = CreateUser()
    if 'password2' in request.POST:
        try:
            createForm = CreateUser(data=request.POST)
            if createForm.is_valid():
                createForm.save()
                return redirect('login')
            else:
                return render(request, 'core/create.html', {'err':'Error in registetering data, please check the fields', 'createForm': createForm})
        except Exception as e:
            print(e)
            return render(request, 'core/create.html', {'err':'Error authenticating, please check your data', 'createForm': createForm})
    return render(request, 'core/create.html', {'createForm': createForm})

def homepage(request):
    return render(request, 'core/homepage.html')

@login_required(login_url='login')
def index(request):
    return render(request, 'core/index.html')

@login_required(login_url='login')
def myEssays(request):
    return render(request, 'core/myEssays.html')

@login_required(login_url='login')
def sendEssays(request):
    return render(request, 'core/sendEssays.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'core/about.html')
    
