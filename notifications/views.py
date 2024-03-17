from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, filters
from .models import Notifications
from .serializers import NotificationsSerializer
from brick_connect_api.permissions import IsNotificationsrecipient


class NotificationsList(generics.ListAPIView):
    
    serializer_class = NotificationsSerializer

    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "read"]
    

    def get_queryset(self):
        return Notifications.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NotificationsDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated, IsNotificationsrecipient]