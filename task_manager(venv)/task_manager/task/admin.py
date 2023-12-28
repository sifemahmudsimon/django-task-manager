from django.contrib import admin

# Register your models here.

from .models import *

class TaskImageInline(admin.TabularInline):
    model = TaskImage
class TaskAdmin(admin.ModelAdmin):
    inlines = [TaskImageInline]
    list_display = ('title','due_date','priority','task_complete','user')
    list_editable = ('due_date','priority','task_complete')

admin.site.register(TaskImage)
admin.site.register(Task,TaskAdmin)