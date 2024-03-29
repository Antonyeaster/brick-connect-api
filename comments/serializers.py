from rest_framework import serializers
from .models import Comment
from comment_like.models import CommentLike
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment Model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    commentlike_id = serializers.SerializerMethodField()
    commentlike_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Returns true if the current user is the owner
        of the comment
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Display time since comment created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Display time elapsed since comment created.
        """
        return naturaltime(obj.updated_at)

    def get_commentlike_id(self, obj):
        """
        Returns the ID of the authenticated user's
        like on the comment.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            commentlike = CommentLike.objects.filter(
                owner=user, comment=obj
            ).first()
            return commentlike.id if commentlike else None
        return None

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'post', 'is_owner', 'profile_id', 'profile_image',
            'content', 'commentlike_id', 'commentlike_count',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for Comment detail view.
    """
    post = serializers.ReadOnlyField(source='post.id')
