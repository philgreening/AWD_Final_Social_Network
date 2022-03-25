from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


from . import api

urlpatterns = [
    path('', TemplateView.as_view(template_name = 'socialApp/index.html'), name='index'),
    path('api/v1/post/<int:pk>', api.PostDetail.as_view(), name='post'),
    path('api/v1/posts/', api.PostList.as_view(), name='posts'),
    path('api/v1/profiles/', api.UserProfileList.as_view(), name='profiles'),
    path('api/v1/profile/<user__username>', api.UserProfileDetail.as_view(), name='profile'),
    path('api/v1/updateprofile/<user__username>', api.UserProfileDetailUpdate.as_view(), name='updateProfile'),
    path('api/v1/search/', api.SearchUsersView.as_view(), name='search'),
    path('api/v1/following_list/', api.FollowerList.as_view() , name='following_list'),
    path('api/v1/following/<int:pk>', api.FollowerDetail.as_view() , name='following')
]