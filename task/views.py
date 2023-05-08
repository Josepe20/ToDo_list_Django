from django.shortcuts import render

# Create your views here.
def list_task(request):
    return render(request, 'list_task.html')

