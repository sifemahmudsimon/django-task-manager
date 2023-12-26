from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html',context={})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() :
            messages.error(request, 'Username or email already exists. Please try a different one.')
            return redirect('signup')  # Redirect back to signup page

        # Create a new User using Django's create_user method
        user = User (
            username=username, 
            email=email,            
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('signin')  # Redirect to login page after successful signup
    else:
        return render(request, 'registration/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('index')  # Redirect to some page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('signin')  # Redirect back to login page for retry

    return render(request,'registration/login.html')

