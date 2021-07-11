from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from users.forms import LoginForm


def index(request):
    context = {
        'form': LoginForm()
    }
    return render(request, 'home.html', context)


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
    return render(request, 'dashboard.html')
