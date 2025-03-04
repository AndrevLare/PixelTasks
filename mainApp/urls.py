from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projectOverview/<int:id>/', views.projectOverview, name='projectOverview'),
    path('deleteProject/<int:id>/', views.deleteProject, name='delete'),
    path('pomodoro/', views.pomodoro, name='pomodoro'),
    # Otras rutas...
]
