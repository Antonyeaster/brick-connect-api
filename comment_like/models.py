from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class CommentLike(models.Model):
    """
    CommentLike model represents a 'like' on a comment.
    It relates to the User and Comment model.
    'owner' relating to the User modal for the
    user that liked the comment.
    'comment' relating to the comment model for the
    comment that has been liked.
    Using 'unique_together' ensures the same user cant like the
    same comment twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
            Comment, related_name='commentlike', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'comment']

    def __str__(self):
        return f'{self.owner} {self.comment}'
