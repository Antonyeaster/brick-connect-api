from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Favourite(models.Model):
    """
    Favourite model relates to the User and Post model
    'owner' is a user who favorited the post.
    'post' is the post that was favorited.
    Using 'unique_together' ensures the same user can't favourite
    the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favourites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['post', 'owner']

    def __str__(self):
        return f'{self.owner} {self.post}'
