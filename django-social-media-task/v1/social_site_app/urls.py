from django.urls import path, include

from .views.user_authentication import *

urlpatterns = [
    path('app/v1/welcome/', welcome, name='welcome'),
    path('', custom_login, name='custom_login'),
    path('api/v1/register/', register_user, name='register_user'),
    path('logout/', user_logout, name='user_logout'),
    # path('app/v1/social-site/profile/<int:user_id>/', view_profile, name='view_profile'),
    # path('app/v1/social-site/profile/edit/', update_profile, name='update_profile'),
]
