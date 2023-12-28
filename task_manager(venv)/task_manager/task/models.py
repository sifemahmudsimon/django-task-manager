from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10,choices=PRIORITY_CHOICES)
    task_complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title
   

class TaskImage(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/taskimages')