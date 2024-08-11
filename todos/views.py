from django.shortcuts import render, redirect
from todos.models import TodoList
from todos.forms import TodoListForm


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


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todolist = form.save(False)
            todolist.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm()

        context = {
            "form": form,
        }
        return render(request, "todos/CreateTodo.html", context)
