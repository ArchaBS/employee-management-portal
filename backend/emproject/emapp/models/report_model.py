from django.db import models
from .user_model import User


class Report(models.Model):

    REPORT_TYPES = (
        ("Attendance", "Attendance"),
        ("Leave", "Leave"),
        ("Task", "Task"),
        ("Project", "Project"),
    )

    report_type = models.CharField(max_length=30, choices=REPORT_TYPES)

    generated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    generated_at = models.DateTimeField(auto_now_add=True)

    file_name = models.CharField(max_length=200)

    def __str__(self):
        return self.file_name