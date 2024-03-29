from rest_framework import serializers
from .models import Post
from likes.models import Like
from favourites.models import Favourite


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    favourite_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Restricts the size of the images.
        """
        if value.size > 1024 * 1024 * 5:
            raise serializers.ValidationError(
                'Image size is larger than 5MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width is larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height is larger than 4096px'
            )
        return value

    def get_is_owner(self, obj):
        """
        Returns true if the current user is the owner
        of the post
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Returns the ID of the authenticated user's
        like on a post.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_favourite_id(self, obj):
        """
        Returns the ID of the authenticated user's
        favourite on a post.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, post=obj
            ).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'description',
            'image', 'is_owner', 'profile_id', 'profile_image', 'image_filter',
            'like_id', 'comments_count', 'likes_count', 'favourite_id',
            'category'
        ]
