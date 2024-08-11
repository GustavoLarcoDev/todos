from django.shortcuts import render
from todos.models import TodoList


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todolist_object": todos
    }
    return render(request, "todos/TodoList.html", context)


def todo_list_detail(request, id):
    list = TodoList.objects.get(id=id)
    context = {
        "list_object": list,
        }
    return render(request, "todos/TodoDetail.html", context)
