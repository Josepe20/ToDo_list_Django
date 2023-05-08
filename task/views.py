from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    return render(request, 'task/list_task.html')

def create_task(request):
    print(request.POST)
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

