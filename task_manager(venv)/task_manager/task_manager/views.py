from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html',context={})

def signup(request):
    return render(request,'registration/signup.html')

def login(request):
    return render(request,'registration/login.html')

