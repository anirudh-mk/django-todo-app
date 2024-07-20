from django.urls import path

from home import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('todo', views.todo, name='todo'),
]
