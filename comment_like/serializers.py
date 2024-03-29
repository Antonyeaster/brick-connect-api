from django.db import IntegrityError
from rest_framework import serializers
from .models import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for CommentLike model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLike
        fields = [
            'id', 'owner', 'created_at', 'comment',
        ]

    def create(self, validated_data):
        """
        Handles possible duplication
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible duplication'
            })
