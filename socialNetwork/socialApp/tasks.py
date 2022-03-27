from email.mime import image
from celery import shared_task
from .models import *
from PIL import Image as img
import io
from django.core.files.uploadedfile import SimpleUploadedFile

# Celery task to create thumbnail of image upload
@shared_task
def make_thumbnail(user_image):
    record = UserProfile.objects.get(pk=user_image)
    
    #stores upload in media folder and resizes image
    image = img.open('media/'+ str(record.profile_image))
    x_scale_factor = image.size[0]/200
    thumbnail = image.resize((200, int(image.size[1]/x_scale_factor)))

    byteArr = io.BytesIO()
    thumbnail.save(byteArr, format='jpeg')
    file = SimpleUploadedFile("thumb_" + str(record.profile_image), byteArr.getvalue())
    record.profile_image = file
    record.save()
