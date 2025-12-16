from django.shortcuts import render, redirect

def home(request):
    return render(request, 'enchere/home.html')

def signup(request):
    return render(request, 'enchere/signup.html')

def login_view(request):
    return render(request, 'enchere/login.html')
