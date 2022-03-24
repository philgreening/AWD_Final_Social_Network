from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)


    def __str__(self):
        return str(self.user.username)
    
class Posts(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(auto_now_add=True)
    post_text = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering = ('-post_date',)

class Following(models.Model):
    user = models.CharField(max_length=200)
    following = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user + ' is following ' + self.following)

