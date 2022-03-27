import factory

from .models import *

# create fixtures for User model
class UserFactory(factory.django.DjangoModelFactory):
    username = 'DarthVader'

    class Meta:
        model = User

# create fixtures for userProfile model
class UserProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    first_name = 'Anakin'
    last_name = 'Skywalker'
    bio = factory.Faker('paragraph', nb_sentences=3)
    profile_image = factory.Faker('file_extension',category='image')
    

    class Meta:
        model = UserProfile

# create fixtures for Posts model
class PostFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    post_date = models.DateTimeField(auto_now_add=True)
    post_text = factory.Faker('sentence', nb_words=10)

    class Meta:
        model = Posts

# create fixtures for Follower model
class FollowerFactory(factory.django.DjangoModelFactory):
    id = 1
    user = 'DarthVader'
    following = 'HanSolo'

    class Meta:
        model = Following
