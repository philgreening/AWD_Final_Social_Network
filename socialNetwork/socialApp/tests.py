import json

from django.urls import reverse
from rest_framework.test import APITestCase

from .model_factories import *
from .models import *
from .serializers import *

#***************************************
#***************API TESTS***************
#***************************************


# tests /api/profile endpoint
class UserProfileTest(APITestCase):
    user = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = UserProfileFactory.create()
        self.good_url = reverse('profile', kwargs= {'user__username' : 'DarthVader'})
        self.bad_url = '/api/profile/1'

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)

    def test_UserDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_UserDetailReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_UserDetailCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertTrue('last_name' in data)

# tests /api/profiles endpoint
class UserProfilesTest(APITestCase):
    user = None
    user2 = None
    user3 = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = UserProfileFactory.create()
        self.user2 = UserProfileFactory.create(pk=2, user__username = 'LukeSkywalker')
        self.user3 = UserProfileFactory.create(pk=3, user__username = 'C3PO')
        self.good_url = reverse('profiles')
        self.bad_url = '/api/userprofiles/'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)
    
    def test_UserProfileListReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_UserProfileListReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
 
    def test_UserProfileListLength(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)
    
    def test_UserProfileListCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        for user in data:
            self.assertTrue('profile_image' in user)

# tests /api/post endpoint
class PostTest(APITestCase):
    user = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = PostFactory.create()
        self.good_url = reverse('post', kwargs= {'pk' : 1})
        self.bad_url = '/api/post/user'

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)

    def test_PostDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_PostDetailReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_PostDetailCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertTrue('post_text' in data)

# tests /api/posts endpoint
class PostsTest(APITestCase):
    user = None
    user2 = None
    user3 = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = PostFactory.create()
        self.user2 = PostFactory.create(pk=2, user__username = 'LukeSkywalker')
        self.user3 = PostFactory.create(pk=3, user__username = 'C3PO')
        self.good_url = reverse('posts')
        self.bad_url = '/api/posts/1'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)
    
    def test_PostsListReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_PostsListReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
 
    def test_PostsListLength(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)
    
    def test_PostsListCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        for post in data:
            self.assertTrue('post_date' in post)

# tests /api/updateprofile/ endpoint

class UpdateProfileTest(APITestCase):
    user = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = UserProfileFactory.create()
        self.good_url = reverse('updateProfile', kwargs= {'user__username' : 'DarthVader'})
        self.bad_url = '/api/update/'

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)

    def test_UpdateUserDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_UpdateUserDetailReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_UpdateUserDetailCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertTrue('last_name' in data)

# tests api/v1/following_list/ endpoint

class FollowersTest(APITestCase):
    user = None
    user2 = None
    user3 = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = FollowerFactory.create()
        self.user2 = FollowerFactory.create(pk=2, user = 'LukeSkywalker')
        self.user3 = FollowerFactory.create(pk=3, user = 'C3PO')
        self.good_url = reverse('following_list')
        self.bad_url = '/api/following/'
    
    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)
    
    def test_FollowerListReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_FollowerListReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
 
    def test_FollowerListLength(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)
    
    def test_FollowerListCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        for follow in data:
            self.assertTrue('following' in follow)

# tests /api/following/ endpoint

class FollowerDetailTest(APITestCase):
    user = None
    good_url = ''
    bad_url = ''

    # set up variables for testing
    def setUp(self):
        self.user = FollowerFactory.create()
        self.good_url = reverse('following', kwargs= {'pk' : 1})
        self.bad_url = '/api/follow/'

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()
        
        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)

    def test_FollowerDetailReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)
    
    def test_FollowerDetailReturnFailOnBadAttribute(self):
        response = self.client.get(self.bad_url, format='json')
        self.assertEqual(response.status_code, 404)
    
    def test_FollowerDetailCheckFieldPresent(self):
        response = self.client.get(self.good_url, format='json')
        data = json.loads(response.content)
        self.assertTrue('user' in data)


# #**********************************************
# #***************SERIALIZER TESTS***************
# #**********************************************


class PostsSerializerTest(APITestCase):
    user = None
    posts_serializer = None

    # set up variable for testing
    def setUp(self):
        self.user = PostFactory.create()
        self.posts_serializer = PostsSerializer(instance=self.user)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()

        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)
    
    def test_PostsSerializer(self):
        data = self.posts_serializer.data
        self.assertEqual(set(data.keys()), set(['user',
                                                'post_date',
                                                'post_text'
                                                ]))
    def test_PostsSerializerUserisOk(self):
        data = self.posts_serializer.data
        self.assertEqual(data['user'], 'DarthVader')

class UserProfileSerializerTest(APITestCase):
    user = None
    profile_serializer = None

    # set up variable for testing
    def setUp(self):
        self.user = UserProfileFactory.create()
        self.profile_serializer = UserProfileSerializer(instance=self.user)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()

        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)
    
    def test_UserProfileSerializer(self):
        data = self.profile_serializer.data
        self.assertEqual(set(data.keys()), set(['user',
                                                'first_name',
                                                'last_name',
                                                'bio',
                                                'profile_image'
                                                ]))
    def test_UserProfileSerializerFirstNameisOk(self):
        data = self.profile_serializer.data
        self.assertEqual(data['first_name'], 'Anakin')

class FollowingSerializerTest(APITestCase):
    user = None
    following_serializer = None

    # set up variable for testing
    def setUp(self):
        self.user = FollowerFactory.create()
        self.following_serializer = FollowingSerializer(instance=self.user)

    # Deletes everything from test database and resets primary key
    def tearDown(self):
        UserProfile.objects.all().delete()
        Posts.objects.all().delete()
        Following.objects.all().delete()

        UserProfileFactory.reset_sequence(0)
        PostFactory.reset_sequence(0)
        FollowerFactory.reset_sequence(0)
    
    def test_FollowingSerializer(self):
        data = self.following_serializer.data
        self.assertEqual(set(data.keys()), set(['id',
                                                'user',
                                                'following'
                                                ]))
    def test_FollowingSerializerIdisOk(self):
        data = self.following_serializer.data
        self.assertEqual(data['id'], 1)