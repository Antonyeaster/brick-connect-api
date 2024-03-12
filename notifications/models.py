from django.db import models
from django.contrib.auth.models import User


class Notifications(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}"
    