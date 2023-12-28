from django.shortcuts import render,redirect
from task.models import Task,TaskImage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.db.models import Q #for complex querry

from datetime import datetime
# Create your views here.
@login_required(login_url='/login/')
def index(request):
    # Retrieve tasks associated with the currently logged-in user
    tasks = Task.objects.filter(user=request.user)
    query = request.GET.get('q')  # Get the search query from the URL parameter
    filter_by = request.GET.get('filter')

    if query:
        # Filter tasks by title containing the search query
        tasks = tasks.filter(Q(title__icontains=query))

    if filter_by == 'creation_date':
        tasks = tasks.order_by('created')  
    elif filter_by == 'due_date':
        tasks = tasks.order_by('due_date')
    elif filter_by == 'priority':
        tasks = tasks.order_by('priority') 
        tasks = sorted(tasks, key=lambda x: ['high', 'medium', 'low'].index(x.priority))
    elif filter_by == 'completed':
        tasks = tasks.filter(task_complete=True)
    elif filter_by == 'active':
        tasks = tasks.filter(task_complete=False)

    context = {
        'tasks': tasks
    }

    if request.method == 'POST':
        task_id = request.POST.get('task_id')  
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
            return redirect('signup')  

        # Create a new User 
        user = User (
            username=username, 
            email=email,            
        )
        user.set_password(password) #set algorithm for password hashing
        user.save()
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login') 
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
            return redirect('index')  
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login') 

    return render(request,'registration/login.html')

@login_required(login_url='/login/')
def task_entry(request):
    if request.method == 'POST':
        # Get all the field values
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date_str = request.POST.get('due_date')
        priority = request.POST.get('priority')
        
        # Ensure the due date is parsed properly
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
        
        # Retrieve the logged-in user
        user = request.user
        
        # Create the Task object associated with the user
        new_task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            user=user  # Associate the task with the logged-in user
        )
        new_task.save()

        images = request.FILES.getlist('image_uploads') 
        for image in images:
            TaskImage.objects.create(task=new_task, image=image)  # Associate each image with the task      
        return redirect('index')
        
      

    return render(request, 'task_app/task_entry.html')


@login_required(login_url='/login/')
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

        if 'delete_task' in request.POST:
            # Perform the deletion action
            task.delete()
            # Optionally, you can redirect the user after deletion
            return redirect('index')
    
        # Handle image uploads
        images = request.FILES.getlist('image_uploads')  # Get list of uploaded images
        for image in images:
            TaskImage.objects.create(task=task, image=image)  # Associate each image with the task    
        return redirect('task_detail', task_id=task.id)
                

    return render(request,'task_app/task_detail.html', context)