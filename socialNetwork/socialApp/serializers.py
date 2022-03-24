from asyncore import read
from rest_framework import serializers
from django.contrib.auth.models import User
from drf_writable_nested.serializers import WritableNestedModelSerializer



from .models import *

class PostsSerializer(serializers.ModelSerializer):
    # allows username to be selected from User model
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    class Meta:
        model = Posts
        fields = [ 'user', 'post_date', 'post_text', 'images']


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    queryset = UserProfile.objects.all()

    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'profile_image' ]

class UpdateProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    queryset = UserProfile.objects.all()
    
    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'profile_image']

class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Following
        fields=['id','user', 'following']




    