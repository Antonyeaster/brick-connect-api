from rest_framework import generics, permissions
from brick_connect_api.permissions import IsOwnerOrReadOnly
from .models import CommentLike
from .serializers import CommentLikeSerializer


class CommentLikeList(generics.ListCreateAPIView):
    """
    Lists all comment likes, if user is authenticated
    they can like a comment.
    """
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CommentLike.objects.all()

    def perform_create(self, serializer):
        """
        This gets the current logged in userand links
        a the like on the comment to their profile.
        """
        serializer.save(owner=self.request.user)


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve or destroys a like on a comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()
