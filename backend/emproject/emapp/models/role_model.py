from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):

    ROLE_CHOICES = [
        ("Manager", "Manager"),
        ("Developer Lead", "Developer Lead"),
        ("Test Lead", "Test Lead"),
        ("Developer", "Developer"),
        ("Tester", "Tester"),
    ]

    role_name = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.role_name