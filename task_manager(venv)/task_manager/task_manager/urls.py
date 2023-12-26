from django.contrib import admin
from django.urls import path
from . import views  # Lowercase 'views'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),

]

