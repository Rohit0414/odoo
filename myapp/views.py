from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm 

def task_list(request):
    tasks = Task.objects.all()  
    form = TaskForm()  
    if request.method == 'POST':
        form = TaskForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('task_list') 
    return render(request, 'myapp/home.html', {'tasks': tasks, 'form': form})  

def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    task.delete() 
    return redirect('task_list')  

def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    task.completed = not task.completed 
    task.save()  
    return redirect('task_list')  
