from django.urls import path
from todolist.views import show_todo,login_user,register,create_task, change_status_task, delete_task,edit_task,logout_user,show_todolist_json,add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todo, name='show_todo'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create_task/', create_task, name='create_task'),
    path('change_status_task/<int:pk>/', change_status_task, name='change'),
    path('delete_task/<int:pk>/', delete_task, name='delete'),
    path('edit_task/<int:pk>/', edit_task, name='edit'),
    path('logout/', logout_user, name='logout'),
    path('json/', show_todolist_json, name="show_todolist_json"),
    path('add_task/', add_task, name="add_task"),
]