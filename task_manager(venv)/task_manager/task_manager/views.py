from django.shortcuts import render,redirect
from task.models import Task,TaskImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.files.base import ContentFile

from datetime import datetime
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    # Retrieve tasks associated with the currently logged-in user
    tasks = Task.objects.filter(user=request.user)
    
    context = {
        'tasks': tasks
    }

    if request.method == 'POST':
        task_id = request.POST.get('task_id')  # Assuming the task_id is sent via POST
        if task_id:
            task = Task.objects.get(pk=task_id)
            task.task_complete = True
            task.save()




    return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists() :
            messages.error(request, 'Username or email already exists. Please try a different one.')
            return redirect('signup')  # Redirect back to signup page

        # Create a new User 
        user = User (
            username=username, 
            email=email,            
        )
        user.set_password(password) #set algorithm for password hashing
        user.save()
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')  # Redirect to login page after successful signup
    else:
        return render(request, 'registration/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
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
            return redirect('login')  # Redirect back to login page for retry

    return render(request,'registration/login.html')

def task_detail(request,task_id):

    task=Task.objects.get(pk=task_id)
    task.due_date_formatted = task.due_date.strftime('%Y-%m-%d')
    context = {
        'task': task
    }
    if request.method == 'POST':
        task.title = request.POST.get('title')  # Update title
        task.description = request.POST.get('description')  # Update description
        
        due_date_str = request.POST.get('due_date')
        if due_date_str:
            task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d')  
            

        task.priority = request.POST.get('priority')  
        task.save()  # Save the updated task

        # Handle image uploads
        if 'image_uploads' in request.FILES:
            images = request.FILES.getlist('image_uploads')  # Get list of uploaded images
            for image in images:
                TaskImage.objects.create(task=task, image=image)  # Associate each image with the task
        messages.success(request, 'Images uploaded successfully!')        
        return redirect('task_detail', task_id=task.id)
                

    return render(request,'task_app/task_detail.html', context)

