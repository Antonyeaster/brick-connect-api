from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, filters
from .models import Notifications
from .serializers import NotificationsSerializer


class NotificationsList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationsSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["read", "created_at"]

    def get_queryset(self):
        return Notifications.objects.filter(recipient=self.request.user, read=False)


class NotificationsDetail(generics.RetrieveUpdateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]