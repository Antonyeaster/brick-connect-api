from rest_framework import serializers
from .models import Notifications
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime
from datetime import timedelta

class NotificationsSerializer(serializers.ModelSerializer):
    recipient = serializers.ReadOnlyField(source="recipient.username")
    sender = serializers.ReadOnlyField(source="sender.username")
    profile_image = serializers.ReadOnlyField(source="sender.profile.image.url")
    created_at = serializers.SerializerMethodField()
    object_id = serializers.ReadOnlyField()

    def get_created_at(self, obj):
        if obj.created_at > timezone.now() - timedelta(days=1):
            return naturaltime(obj.created_at)
        else:
            return obj.created_at.strftime("%d %b %Y, %I:%M %p")

    class Meta:
        model = Notifications
        fields = ['id', 'recipient', 'sender', 'text', 'created_at', 'read', 'category', 'profile_image', 'object_id',]