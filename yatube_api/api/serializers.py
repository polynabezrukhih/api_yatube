
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Post"""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Comment"""
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    """Сериалайзер модели Group"""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)
        read_only_fields = ('id',)
