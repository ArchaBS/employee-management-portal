from django.db import models
from django.conf import settings


class ActivityLog(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="activity_logs"
    )

    module = models.CharField(max_length=100)

    action = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        ordering = ["-timestamp"]
        verbose_name = "Activity Log"
        verbose_name_plural = "Activity Logs"

    def __str__(self):
        return f"{self.user.username} | {self.module} | {self.action}"