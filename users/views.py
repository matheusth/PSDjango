from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'home.html')


def auth_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if not user:
            return redirect('index')

        login(request, user)
        return redirect('dashboard')


def dashboard(request):
    return render(request, 'home.html')
