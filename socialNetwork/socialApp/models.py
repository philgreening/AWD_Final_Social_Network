from distutils.command.upload import upload
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    def __str__(self):
        return self.user.username

class Posts(models.Model):
    # postId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    post_date = models.DateField(auto_now_add=True)
    post_text = models.CharField(max_length=250)
    likes = models.IntegerField(null=True)
    images = models.ImageField(upload_to='post_images', blank=True)

    def __str__(self):
        return self.user.username

