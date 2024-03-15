from django.db import models
from django.conf import settings


class Notifications(models.Model):

    CATEGORY_CHOICES = (
        ("follow", "Follow"),
        ("comment", "Comment"),
    )

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sent_notifications")
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default='')
    object_id = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.username} -> {self.recipient.username}"
    