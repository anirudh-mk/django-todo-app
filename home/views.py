from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from home.models import Todo, UserTodoLink


# Create your views here.


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('todo')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if email and username and password and confirm_password:
            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exists')
                    return redirect('register')

                if User.objects.filter(email=email).exists():
                    messages.info(request, 'email already exists')
                    return redirect('register')

                else:
                    user = User.objects.create_user(email=email, username=username, password=password, first_name=name)
                    user.save()
                    return redirect('login')
            else:
                messages.info(request, 'password doesnot match')
                return redirect('register')
        else:
            messages.info(request, 'all fields required')
    else:
        return render(request, 'register.html')


@login_required(login_url='login')
def todo(request):
    user = request.user

    if request.method == 'POST':
        name = request.POST['todo_name']
        description = request.POST['todo_description']
        status = 'Pending'

        task = Todo(name=name, description=description, status=status, user=user)
        task.save()

        # user_todo_link = UserTodoLink(todo=task, user=user)
        # user_todo_link.save()

        return redirect('todo')

    else:

        task = Todo.objects.filter(user=user).all()

        return render(request, 'todo.html', {'todos': task})


def logout(request):
    auth.logout(request)
    return redirect('login')


def complete(request):
    id = request.GET.get('id')
    Todo.objects.filter(id=id).update(status='Completed')
    return redirect('todo')


def delete(request):
    id = request.GET.get('id')
    Todo.objects.filter(id=id).delete()
    return redirect('todo')
