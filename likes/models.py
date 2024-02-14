from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Like(models.Model):
    """
    Like model relates to the User and Post model
    The owner is a user instance and the post is a post instance
    Using 'unique_together' ensures the same user cant like the
    same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
