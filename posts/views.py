from rest_framework import generics, permissions, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from brick_connect_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response


class CategoriesView(generics.ListCreateAPIView):
    """
    List and create posts filtered by a category
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def post(self, request):
        data = self.request.data
        category = data['category']
        queryset = Post.objects.order_by(
            '-created_at').filter(category__iexact=category)

        serializer = PostSerializer(queryset, many=True)

        return Response(serializer.data)


class PostList(generics.ListCreateAPIView):
    """
    Retrieve and create posts
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # User feed shows posts from Users being followed
        'owner__followed__owner__profile',
        # Get posts liked by current User
        'likes__owner__profile',
        # Get posts owned by specific User
        'owner__profile',
        # Get posts favourited by current User
        'favourites__owner__profile',
        'favourites',
        # Filter posts based on their category
        'category',
    ]

    search_fields = [
        'owner__username',
        'title',
        'category',
    ]

    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
        'favourites__created_at',
    ]

    def perform_create(self, serializer):
        """
        If user is signed in, this saves the
        new post to database.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit or delete if you are the owner.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
