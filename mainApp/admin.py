from django.contrib import admin

from .models import Task, Project

admin.site.site_header = "PixelTasks Admin"
admin.site.site_title = "PixelTasks Admin Portal"
admin.site.index_title = "Welcome to PixelTasks Researcher Portal"
admin.site.register(Task)
admin.site.register(Project)