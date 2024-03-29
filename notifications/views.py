from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, filters
from .models import Notifications
from .serializers import NotificationsSerializer
from brick_connect_api.permissions import IsNotificationsrecipient


class NotificationsList(generics.ListAPIView):
    """
    Lists the notification for the authenticated user
    that owns the profile related to the notifications.
    Notification creates automatically, this is why the
    create view is missing
    """
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "read"]

    def get_queryset(self):
        return Notifications.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotificationsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or delete the notification, user must the the
    authenticated owner
    """
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [
            permissions.IsAuthenticated, IsNotificationsrecipient]
