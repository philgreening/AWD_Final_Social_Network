from rest_framework import serializers

from .models import *

class PostsSerializer(serializers.ModelSerializer):
    # allows username to be selected from User model
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    class Meta:
        model = Posts
        fields = [ 'user', 'post_date', 'post_text', 'likes', 'images']

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'profile_image', 'followers', 'follows']
   



