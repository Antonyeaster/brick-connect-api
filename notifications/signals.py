from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from comments.models import Comment
from followers.models import Follower
from .models import Notifications


def create_notification(**kwargs):
    Notifications.objects.create(
        owner=kwargs["owner"],
        sender=kwargs["sender"],
        category=kwargs["category"],
        object_id=kwargs["object_id"],
        text=kwargs["text"],
    )

@receiver(post_save, sender=Follower)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        data = {
            "owner": instance.followed,
            "sender": instance.owner,
            "category": "follow",
            "object_id": instance.id,
            "text": f"{instance.owner.username} started following you.",
        }

        create_notification(**data)

@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        data = {
            "owner": instance.post.owner,
            "sender": instance.owner,
            "category": "comment",
            "object_id": instance.post.id,
            "text": f"{instance.owner.username} commented on your post "
            f"{instance.post.title}",
        }

        create_notification(**data)