"""socialNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('socialApp.urls')),
    path('admin/', admin.site.urls),
    # includes djoser api links and authentication api endpoints 
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    # generate open-api schema and link
    path('apischema/', get_schema_view(
        title= 'YourSpace REST API',
        description= 'API for interacting with YourSpace user records',
        version='1.0'
    ), name='openapi-schema'),
    # generate API documentation and link
    path('swaggerdocs/', TemplateView.as_view(
        template_name = 'socialApp/swagger-docs.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui' )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
