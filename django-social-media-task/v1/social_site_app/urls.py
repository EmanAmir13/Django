from django.urls import path, include

from .views import *
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
    path('app/v1/post/create/', create_post, name='create_post'),
    path('app/v1/post/view/', view_posts, name='view_posts'),
    path('app/v1/post/edit/<int:post_id>/', edit_post, name='edit_post'),
    path('app/v1/post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('app/v1/post/view_own_posts/', view_own_posts, name='view_own_posts'),

]
