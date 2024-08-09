from django.shortcuts import render
from todos.models import TodoList


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todolist_object": todos
    }
    return render(request, "todos/TodoList.html", context)
