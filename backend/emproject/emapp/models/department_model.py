from django.db import models
from django.contrib.auth.models import AbstractUser

class Department(models.Model):

    department_name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.department_name