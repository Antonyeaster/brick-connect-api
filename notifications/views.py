from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, filters
from .models import Notifications
from .serializers import NotificationsSerializer


class NotificationsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationsSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["read", "created_at"]

    def get_queryset(self):
        return Notifications.objects.filter(recipient=self.request.user)

    def perform_create(self, serializer):

        read_value = self.request.data.get('read', '').lower() == 'true'
        
        serializer.save(
            recipient=self.request.user,
            sender=self.request.user,
            read=read_value,
            category=self.request.data.get('category', ''),
            object_id=self.request.data.get('object_id', None),
        )

class NotificationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [permissions.IsAuthenticated]