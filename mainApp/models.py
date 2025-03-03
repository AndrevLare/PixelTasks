from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    progress = models.IntegerField()
    creation_date = models.DateField()
    last_update = models.DateField()

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title