from django.shortcuts import render

from .models import Project

def dashboard(request):
    
    projects = Project.objects.all()
    
    return render(request, 'dashboard.html', {'projects': projects})

def proyectOverview(request):
    return render(request, 'mainApp/proyectOverview.html')

def pomodoro(request):
    return render(request, 'mainApp/pomodoro.html')
