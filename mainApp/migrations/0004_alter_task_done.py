# Generated by Django 5.1.6 on 2025-03-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_rename_projects_project_rename_tasks_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
