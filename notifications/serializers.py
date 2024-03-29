from rest_framework import serializers
from .models import Notifications
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime
from datetime import timedelta


class NotificationsSerializer(serializers.ModelSerializer):
    """
    Serializer for notification model, displays created at
    In a more readable format.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    sender = serializers.ReadOnlyField(source="sender.username")
    profile_image = serializers.ReadOnlyField(
        source="sender.profile.image.url"
    )
    object_id = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        if obj.created_at > timezone.now() - timedelta(days=1):
            return naturaltime(obj.created_at)
        else:
            return obj.created_at.strftime("%d %b %Y, %I:%M %p")

    class Meta:
        model = Notifications
        fields = [
            "id",
            "owner",
            "sender",
            "profile_image",
            "created_at",
            "object_id",
            "read",
            "text",
            "category",
        ]
