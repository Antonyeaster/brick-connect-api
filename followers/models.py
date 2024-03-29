from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model relates to owner and followed.
    'owner' is a user that is following another user.
    'followed' is a user that is followed by the owner.
    The 'related_name' makes sure django can tell the
    difference between owner and followed.
    Using 'unique_together' ensures users can follow the
    same account more then once
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
