from django.urls import path
from . import views
from django.views.decorators.http import require_POST

# urlpatterns = [
#     path('todo/', views.TodoList.as_view()),
#     path('todo/<int:pk>', views.TodoDetail.as_view()),
# ]

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('update/<int:primary_key>/', views.todo_update, name='todo_update'),
    path('delete/<int:primary_key>/', views.todo_delete, name='todo_delete'),
    path('complete/<int:primary_key>', require_POST(views.todo_complete)),
]
