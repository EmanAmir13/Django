from django.urls import path, include
from .social_site import urls as social_site_urls

urlpatterns = [
    path('app/v1/social-site/', include(social_site_urls)),
]
