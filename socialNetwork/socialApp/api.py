from pyparsing import FollowedBy
from .models import *
from .serializers import *
from django.db.models import Q

from rest_framework import generics
from rest_framework import mixins

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostDetail(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView,):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostListFollows(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


    def get_queryset(self):

        post_list = UserProfile.objects.filter(
            user='user')
        
        return post_list


    

class UserProfileDetail(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'

    # def patch(self):
    #     user = self.kwargs.get('user__username')
    #     profile = UserProfile.objects.patch(user=user)
    #     print("profile",profile)
    #     return profile
     


class UserProfileDetailUpdate(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UpdateProfileSerializer
    lookup_field = 'user__username'

    
    # lookup_field = 'user__username'

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def update(self, request):
    #     print(request)
    #     profile = UserProfile.objects.get(user=request)
    #     profile.followed_by.add(user)
    
#     def update(request,loggedin_user,user):
#         '''
#         Purpose: Follow the user
#         Input: -
#         Output: User object of the logged in user
#         '''
#         try:
#             cur_user=UserProfile.objects.get(username=loggedin_user)
#             fol_user=UserProfile.objects.get(username=user)
#             cur_user.following.add(fol_user)
#             cur_user.save()
#             serializer = UserProfileSerializer(cur_user)
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
#         except Exception as e:
#             error = {'Error_code': status.HTTP_400_BAD_REQUEST,
#                             'Error_Message': "Request Failed. Invalid Details"}
#             return Response(error, status=status.HTTP_400_BAD_REQUEST)  
        


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)

class SearchUsersView(generics.ListCreateAPIView):
    model = UserProfile
    serializer_class = UserProfileSerializer

   
    def get_queryset(self):
        query = self.request.GET.get('q')
        user_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )
        return user_list
