from django.contrib import admin

from .models import *

admin.site.register(UserProfile)
admin.site.register(Posts)
admin.site.register(Following)