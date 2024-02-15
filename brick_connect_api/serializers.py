from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Retrieves users details to display when they log in
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """
        Fields to be displayed
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )