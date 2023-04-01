from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )

    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    validators = [
        serializers.UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following'],
            message='Подписка на себя дважы невозможна.'
        )
    ]

    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Подписка на себя невозможна.'
            )
        return value

    class Meta:
        model = Follow
        fields = ('user', 'following')
