from django.dispatch import receiver
from django.db.models.signals import post_save
from comments.models import Comment
from followers.models import Follower
from .models import Notifications


def create_notification(**kwargs):
    Notification.objects.create(
        recipient=kwargs["recipient"],
        sender=kwargs["sender"],
        category=kwargs["category"],
        text=kwargs["content"],
    )

@receiver(post_save, sender=Follow)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        Notifications.objects.create(
            recipient=instance.followed_user,
            sender=instance.follower,
            text=f"{instance.follower.username} started following you.",
            category=Notifications.FOLLOW
        )

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        Notifications.objects.create(
            recipient=instance.post.author,
            sender=instance.author,
            text=f"{instance.author.username} commented on your post: {instance.text}",
            category=Notifications.COMMENT
        )