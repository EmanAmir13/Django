# profiles/urls.py
from django.urls import path
from .views import signup, edit_profile, user_login, user_logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile'),
]
