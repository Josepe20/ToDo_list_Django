from django.urls import path
from .views import list_task, create_task, delete_task, update_task, singup, singout, singin, complete_task, list_task_completed, home

urlpatterns = [
    path('', home),
    path('tasks/', list_task, name='tasks_uncompleted'),
    path('tasks_completed/', list_task_completed, name='tasks_completed'),
    path('singup/', singup, name='singup'),
    path('logout/', singout, name='logout'),
    path('login/', singin, name='login'),
    path('new_task/', create_task, name='create_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
