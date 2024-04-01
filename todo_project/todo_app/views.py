from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages


def index(request):
    # Adding Todo's
    if 'todo' in request.GET:
        if len(request.GET['todo']) > 0:
            todo = request.GET['todo']
            add_todo = Todo(todo=todo)
            add_todo.save()
            messages.success(request, 'Todo added successfully')
            return redirect('index')
        
    # Displaying Todo's
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }

    return render(request, 'index.html', context)

def update_todo(request, todoid):
    todo = Todo.objects.filter(id=todoid)

    # Updating a Todo
    if 'update-todo' in request.GET:
        if len(request.GET['update-todo']) > 0:
            updated_todo = request.GET['update-todo']
            todo.update(todo=updated_todo)
            messages.success(request, 'Todo updated successfully')
            return redirect('index')

    context = {
        'todo': todo[0],
    }
    return render(request, 'update.html', context)

def delete_todo(request, todoid):
    # Deleting a Todo
    todo = Todo.objects.filter(id=todoid)
    todo.delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('index')
    