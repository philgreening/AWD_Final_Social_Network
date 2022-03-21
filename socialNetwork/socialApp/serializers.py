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
        fields = [ 'user', 'post_date', 'post_text', 'likes', 'images']


class RelationshipSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')
    # username = serializers.Field(source="user.username")
    # print(user)
    queryset = UserProfile.objects.all()


    class Meta:
        model = UserProfile
        fields = ['user']

class UserProfileSerializer(WritableNestedModelSerializer):
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    # following = serializers.ListField(
    #     child=serializers.CharField(max_length=30), write_only=True)
    following = RelationshipSerializer(many=True)

    queryset = UserProfile.objects.all()
    
    # def update(self, instance, validated_data):
    #     print(validated_data, ':val')
    #     following = validated_data.pop('user')
    #     print(following ,":following")
    #     user_obj = UserProfile.objects.filter(user=following)
    #     print(user_obj)
    #     if user_obj:
    #         instance.following.set(user_obj)
    #         print(instance)
    #     return super().update(instance, validated_data)


    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'profile_image', 'followed_by', 'following', ]

class UpdateProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset= User.objects.all(), slug_field='username')

    queryset = UserProfile.objects.all()
    
    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 'bio', 'profile_image']




    