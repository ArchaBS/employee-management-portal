from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_model import User

class Project(models.Model):
    STATUS_CHOICES = [
    ('NOT_STARTED', 'Not Started'),
    ('IN_PROGRESS', 'In Progress'),
    ('COMPLETED', 'Completed'),
    ('ON_HOLD', 'On Hold'),
]

    project_name = models.CharField(max_length=200)
    project_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    manager = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='managed_projects'
    )

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Not Started'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name