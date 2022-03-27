from .models import *
from .serializers import *
from .tasks import *
from django.db.models import Q

from rest_framework import generics
from rest_framework import mixins

from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser

# Api view for unique posts. allows get, post, delete and put requests
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

# Api view for list of posts. allows get and post requests
class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    

# Api view for unique profiles. allows get, post and put requests
class UserProfileDetail(generics.RetrieveUpdateAPIView, generics.CreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    # allows file uploads
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

# Api view for updating profiles. allows get put/patch requests
class UserProfileDetailUpdate(generics.RetrieveUpdateAPIView, generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user__username'
    # allows file uploads
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    # initiates celery task to create thumbnail
    def perform_update(self, serializer):
        record = serializer.save()
        make_thumbnail.delay(record.pk)

    # initiates celery task to create thumbnail
    def perform_create(self, serializer):
        record = serializer.save()
        make_thumbnail.delay(record.pk)

# Api view for list of profiles. allows get and post requests
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Api view to allow searches to be pefoirmed on user profiles
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

# # Api view for list of follower relationships. allows get and post requests
class FollowerList(generics.ListCreateAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

# # Api view for unique follower relationship. allows get and delete requests
class FollowerDetail(generics.RetrieveDestroyAPIView):
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer
