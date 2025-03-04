from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    progress = models.IntegerField(default=0)

    def update_progress(self):
        total_tasks = self.task_set.count()
        completed_tasks = self.task_set.filter(done=True).count()
        if total_tasks > 0:
            self.progress = (completed_tasks / total_tasks) * 100
        else:
            self.progress = 0
        self.save()

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + str(self.done)