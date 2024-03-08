from rest_framework import generics, permissions
from brick_connect_api.permissions import IsOwnerOrReadOnly
from .models import CommentLike
from .serializers import CommentLikeSerializer


class CommentLikeList(generics.ListCreateAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()
