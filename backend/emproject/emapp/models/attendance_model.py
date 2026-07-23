from django.db import models
from .user_model import User


class Attendance(models.Model):

    STATUS_CHOICES = [
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Half Day", "Half Day"),
        ("Leave", "Leave"),
    ]

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="attendance"
    )

    date = models.DateField()

    check_in = models.TimeField(null=True, blank=True)

    check_out = models.TimeField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Present"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.username} - {self.date}"