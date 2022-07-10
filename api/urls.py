from django.urls import path
from .views import (api_overview, get_todos, get_todo_detail,add_todo, update_todo, delete_todo)

urlpatterns = [
    path('', api_overview, name='api_overview'),
    path('list/', get_todos, name='get_todos'),
    path('<int:pk>/', get_todo_detail, name='get_todo_detail'),
    path('create/', add_todo, name='add_todo'),
    path('update/', update_todo, name='update_todo'),
    path('delete/', delete_todo, name='delete_todo'),
]