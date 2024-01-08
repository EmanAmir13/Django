from django.urls import path, include

from .views import *
from .views.followers_view import *
from .views.user_authentication import *
from .views.profile_view import *

urlpatterns = [
    path('', sign_in, name='sign_in'),
    path('logout/', user_logout, name='user_logout'),
    path('api/v1/dashboard/', welcome, name='welcome'),
    path('api/v1/register/', register_user, name='register_user'),
    path('api/v1/profile/', include([
        path('create/', create_profile, name='create_profile'),
        path('view/', view_profile, name='view_profile'),
        path('edit/', edit_profile, name='edit_profile'),
        path('users/', users_list, name='users_list'),
        path('follow-profile/<str:email>/', follow_profile, name='follow_profile'),
        path('unfollow-profile/<str:email>/', unfollow_profile, name='unfollow_profile'),
        path('user/<str:email>/', view_other_profile, name='view_other_profile'),
    ])),
    path('api/v1/post/', include([
        path('create/', create_post, name='create_post'),
        path('followers-posts/', view_posts, name='view_posts'),
        path('edit/<int:post_id>/', edit_post, name='edit_post'),
        path('delete/<int:post_id>/', delete_post, name='delete_post'),
        path('your-posts/', view_own_posts, name='view_own_posts'),
    ])),
]
