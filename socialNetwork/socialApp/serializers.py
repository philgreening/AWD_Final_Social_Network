from rest_framework import serializers

from .models import *

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['postId', 'user', 'post_date', 'post_text', 'likes', 'images']

