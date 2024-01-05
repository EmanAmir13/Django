# views.py

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from social_site_app.models import UserProfile, UserPost


# views.py

@login_required
def follow_profile(request, email):
    user_to_follow = get_object_or_404(UserProfile, user__email=email)
    request.user.userprofile.followers.add(user_to_follow.user)
    print(f"Followed user: {user_to_follow.user.email}")
    return redirect('users_list')



@login_required
def unfollow_profile(request, email):
    user_to_unfollow = get_object_or_404(UserProfile, user__email=email)
    request.user.userprofile.followers.remove(user_to_unfollow.user)
    print(f"Unfollowed user: {user_to_unfollow.user.email}")
    return redirect('users_list')
