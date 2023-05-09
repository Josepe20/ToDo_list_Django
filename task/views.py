from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'task/list_task.html', {'tasks': tasks})

def create_task(request):
    print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.POST:
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('/tasks/')
    return render(request, 'task/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('/tasks/')
