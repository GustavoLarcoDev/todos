from django.shortcuts import render, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


def todo_list_list(request):
    todos = TodoList.objects.all()
    context = {
        "todolist_object": todos
    }
    return render(request, "todos/TodoList.html", context)


def todo_list_detail(request, id):
    todo_list = TodoList.objects.get(id=id)
    context = {
        "todo_list": todo_list,
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


def todo_list_update(request, id):
    todolist = TodoList.objects.get(id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todolist)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm(instance=todolist)
        context = {
            "todolist_edit": todolist,
            "form": form
        }
    return render(request, "todos/UpdateTodo.html", context)


def todo_list_delete(request, id):
    todolist = TodoList.objects.get(id=id)
    if request.method == "POST":
        todolist.delete()
        return redirect("todo_list_list")
    return render(request, "todos/DeleteTodo.html")


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todoitem = form.save(False)
            todoitem.save()
            return redirect("todo_list_detail", id=todoitem.list.id)
    else:
        form = TodoItemForm()

        context = {
            "form": form,
        }
        return render(request, "todos/CreateItem.html", context)


def todo_item_update(request, id):
    todoitem = TodoItem.objects.get(id=id)
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=todoitem)
        if form.is_valid():
            todoitem = form.save()
            return redirect("todo_list_detail", id=todoitem.list.id)
    else:
        form = TodoItemForm(instance=todoitem)
        context = {
            "todoitem_edit": todoitem,
            "form": form
        }
    return render(request, "todos/UpdateItem.html", context)
