from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']

class CommentSerializer(serializers.ModelSerializer):
    #author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'post']

    """ def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['post'] = {
            'id': instance.post.id,
            'title': instance.post.title,
            'content': instance.post.content,
            'author': instance.post.author.username
            
        }
        return representation """
        