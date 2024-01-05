from django.urls import path, include

from .views import *
from .views.followers_view import *
from .views.user_authentication import *
from .views.profile_view import *

urlpatterns = [
    path('', custom_login, name='custom_login'),
    path('logout/', user_logout, name='user_logout'),
    path('app/v1/welcome/', welcome, name='welcome'),
    path('app/v1/register/', register_user, name='register_user'),
    path('app/v1/profile/create/', create_profile, name='create_profile'),
    path('app/v1/profile/view/', view_profile, name='view_profile'),
    path('app/v1/profile/edit/', edit_profile, name='edit_profile'),
    path('app/v1/profile/delete/', delete_profile, name='delete_profile'),
    path('app/v1/profile/users-list/', users_list, name='users_list'),
    path('app/v1/profile/follow-profile/<str:email>/', follow_profile, name='follow_profile'),
    path('app/v1/profile/unfollow-profile/<str:email>/', unfollow_profile, name='unfollow_profile'),
    path('app/v1/profile/view_other_profile/<str:email>/', view_other_profile, name='view_other_profile'),
    path('app/v1/post/create/', create_post, name='create_post'),
    path('app/v1/post/view/', view_posts, name='view_posts'),
    path('app/v1/post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('app/v1/post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('app/v1/post/view_own_posts/', view_own_posts, name='view_own_posts'),

]
