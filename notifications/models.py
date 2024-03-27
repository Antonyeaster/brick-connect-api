from django.db import models
from django.contrib.auth.models import User

    
class Notifications(models.Model):

    CATEGORIES = [
        ("follow", "Follow"),
        ("comment", "Comment"),
    ]
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_notifications"
    )
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='sent_notifications')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(choices=CATEGORIES, max_length=50)
    object_id = models.IntegerField(null=True)
    read = models.BooleanField(default=False)
    text = models.CharField(max_length=255)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.id} {self.get_category_display()} "
            f"notification for {self.owner}"
        )
