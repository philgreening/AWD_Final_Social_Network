from ast import BinOp
from pyexpat import model
import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from random import randint

from factory.base import Factory

from .models import *

class UserFactory(factory.django.DjangoModelFactory):
    username = 'DarthVader'

    class Meta:
        model = User


# create fixtures for sequencing model
class UserProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    first_name = 'Anakin'
    last_name = 'Skywalker'
    bio = factory.Faker('paragraph', nb_sentences=3)
    profile_image = factory.Faker('file_extension',category='image')
    

    class Meta:
        model = UserProfile

# create fixtures for pfamDescriptions model
class PostFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    post_date = models.DateTimeField(auto_now_add=True)
    post_text = factory.Faker('sentence', nb_words=10)
    # likes = randint(0,4000)
    images = factory.Faker('file_extension',category='image')

    class Meta:
        model = Posts

class FollowerFactory(factory.django.DjangoModelFactory):
    user = 'DarthVader'
    following = 'HanSolo'

    class Meta:
        model = Following
