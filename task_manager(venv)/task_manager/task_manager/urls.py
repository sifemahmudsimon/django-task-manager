from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
from . import views  # Lowercase 'views'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='signin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('task-detail/<int:task_id>/',views.task_detail,name='task_detail'),
    path("task_entry/", views.task_entry, name="task_entry")

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # media file serving configuration 

