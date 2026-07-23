from django.db import models
from django.contrib.auth.models import AbstractUser

from .role_model import Role
from .department_model import Department

class User(AbstractUser):

    employee_id = models.CharField(
        max_length=20,
        unique=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    profile_picture = models.URLField(
    blank=True,
    null=True
)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username