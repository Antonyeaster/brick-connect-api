from django.db import IntegrityError
from rest_framework import serializers
from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """
    Favourite Model serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favourite
        fields = [
            'id', 'owner', 'created_at', 'post',
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
