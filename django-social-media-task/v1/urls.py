from django.urls import path, include
from v1.social_site_app import urls as social_site_urls

urlpatterns = [
    path('', include(social_site_urls)),
]
