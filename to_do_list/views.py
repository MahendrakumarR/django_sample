from django.shortcuts import render, redirect
from .models import ToDoItem  # Use a relative import here
from .forms import ToDoForm
from django.shortcuts import get_object_or_404


def todo_list(request):
    todos = ToDoItem.objects.all()
    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    return render(request, 'to_do_list/todo_list.html', {'todos': todos, 'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(ToDoItem, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return redirect('todo_list')  # Redirect back to the todo list

