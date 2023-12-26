from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views  # Lowercase 'views'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.signin,name='signin'),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # media file serving configuration 

