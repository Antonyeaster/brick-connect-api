from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework import generics, permissions, filters
from brick_connect_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.annotate(
        commentlike_count=Count('commentlike', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'post',
        'commentlike__owner__profile'
    ]

    ordering_fields = [
        'commentlike_count',
        'commentlike__created_at',
    ]


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.annotate(
        commentlikes_count=Count('commentlike', distinct=True)
    ).order_by('-created_at')
