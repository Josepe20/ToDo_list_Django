from django.urls import path
from .views import list_task, create_task, delete_task, update_task, singup, singout, singin

urlpatterns = [
    path('', list_task),
    path('singup/', singup, name='singup'),
    path('logout/', singout, name='logout'),
    path('login/', singin, name='login'),
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
]
