from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()  # Получение всех задач
    return render(request, 'HW11/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'HW11/task_detail.html', {'task': task})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect(reverse('task-list'))  # перенаправление на страницу деталей задачи
    else:
        form = TaskForm()
    return render(request, 'HW11/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect(reverse('task-list'))
    else:
        form = TaskForm(instance=task)
    return render(request, 'HW11/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect(reverse('task-list'))  # возврат к списку задач после удаления
