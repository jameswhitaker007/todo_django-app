from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from .forms import TodoForm
from django.http import JsonResponse

# Create your views here.
# class TodoList(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# class TodoDetail(generics.RetrieveDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', { 'todos': todos })

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_update(request, primary_key):
    todo = Todo.objects.get(id=primary_key)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
        print(form.instance.id)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, primary_key):
    todo = Todo.objects.get(id=primary_key)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'todo': todo})

def todo_complete(request, primary_key):
    todo = Todo.objects.get(id=primary_key)
    todo.completed = not todo.completed
    todo.save()
    return JsonResponse({'message': 'Value updated'})