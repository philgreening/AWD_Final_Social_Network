from .models import *
from .serializers import *
from .tasks import *
from django.db.models import Q

from rest_framework import generics
from rest_framework import mixins

from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser


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

class UserProfileDetail(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)


class UserProfileDetailUpdate(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)


    def perform_update(self, serializer):
        record = serializer.save()
        make_thumbnail.delay(record.pk)

    def perform_create(self, serializer):
        record = serializer.save()
        make_thumbnail.delay(record.pk)


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class SearchUsersView(generics.ListCreateAPIView):
    model = UserProfile
    serializer_class = UserProfileSerializer

    # defines search query set to search on username
    def get_queryset(self):
        query = self.request.GET.get('q')
        user_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )
        return user_list

# 
class FollowerList(generics.ListCreateAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

class FollowerDetail(generics.RetrieveDestroyAPIView):

    queryset = Following.objects.all()
    serializer_class = FollowingSerializer
