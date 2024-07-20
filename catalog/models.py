from django.contrib.auth.models import AbstractUser
from django.db import models

from taskManager import settings


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    PRIORITY_CHOICES = {
        "URGENT": "Urgent",
        "HIGH": "High",
        "MEDIUM": "Medium",
        "LOW": "Low",
    }
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="LOW",
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="tasks"
    )

    class Meta:
        ordering = ("deadline",)

    def __str__(self):
        return self.name
