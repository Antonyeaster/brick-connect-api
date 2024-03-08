from rest_framework import serializers
from .models import Comment
from comment_like.models import CommentLike


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    commentlike_id = serializers.SerializerMethodField()
    commentlike_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_commentlike_id(self, obj):
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
            'post', 'is_owner', 'profile_id', 'profile_image', 'content', 'commentlike_id', 'commentlike_count',
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')