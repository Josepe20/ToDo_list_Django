from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .models import Task


# singup users
def singup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()

                login(request, user)
                return redirect('/')

            except IntegrityError:
                return render(request, 'task/sing_up.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exist',
                })
        else:
            return render(request, 'task/sing_up.html', {
                'form': UserCreationForm,
                'error': 'Passwords do not match',
            })

    return render(request, 'task/sing_up.html', {
        'form': UserCreationForm
    })


def singin(request):
    if request.method == 'POST':

        user = authenticate(
                    request,
                    username=request.POST['username'],
                    password=request.POST['password'])

        if user is None:
            return render(request, 'task/sing_in.html', {
                'form': AuthenticationForm,
                'error': "User Name or Password is incorrect"
            })
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'task/sing_in.html', {
        'form': AuthenticationForm
    })


def singout(request):
    logout(request)
    return redirect('/')


# Create your views here.
def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'task/list_task.html', {'tasks': tasks})


def create_task(request):
    print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/')


def update_page(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task/update_task.html', {'task': task})


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    task.title = request.POST['title']
    task.description = request.POST['description']
    task.save()

    return redirect('/')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/')
