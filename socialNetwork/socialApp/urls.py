from django.contrib import admin
from django.urls import path, include
from . import api

urlpatterns = [
    path('api/v1/post/<int:pk>', api.PostDetail.as_view(), name='post'),
    path('api/v1/posts/', api.PostList.as_view(), name='posts'),
    path('api/v1/profiles/', api.UserProfileList.as_view(), name='profiles'),
]
