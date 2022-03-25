from __future__ import absolute_import
import os
from celery import Celery

# Set up celery and and link to Redis 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialNetwork.settings')
app = Celery('socialNetwork', broker='redis://localhost/', backend='redis://localhost/')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()