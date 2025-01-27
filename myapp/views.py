from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm  # Correct capitalization

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks
    form = TaskForm()  # Initialize the form
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Correct form name
        if form.is_valid():
            form.save()  # Save the new task
            return redirect('task_list')  # Redirect to task list after saving
    return render(request, 'myapp/home.html', {'tasks': tasks, 'form': form})  # Pass tasks and form to template

def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by id
    task.delete()  # Delete the task
    return redirect('task_list')  # Redirect to task list after deletion

def task_update(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by id
    task.completed = not task.completed  # Toggle the completed status
    task.save()  # Save the updated task
    return redirect('task_list')  # Redirect to task list after updating

