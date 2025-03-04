from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from .models import Project, Task
from .forms import ProjectForm, TaskForm

def dashboard(request):
    projects = Project.objects.all()
    
    for project in projects:
        project.update_progress()
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
    
    return render(request, 'dashboard.html', {'projects': projects, 'form': form})

def projectOverview(request, id):
    project = get_object_or_404(Project, id=id)
    project.update_progress()
    tasks = project.task_set.all()
    
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            data = json.loads(request.body)
            task_id = data.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.done = not task.done
            task.save()
            return JsonResponse({'status': 'success'})
        elif 'title' in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.project = project
                task.save()
                return redirect('projectOverview', id=id)
    
    form = TaskForm()
    return render(request, 'projectOverview.html', {'project': project, 'tasks': tasks, 'form': form})

def deleteProject(request, id):
    project = get_object_or_404(Project, id=id)
    project.delete()

def pomodoro(request):
    return render(request, 'pomodoro.html')
