from .models import *
from .serializers import *

from rest_framework import generics
from rest_framework import mixins



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

class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)