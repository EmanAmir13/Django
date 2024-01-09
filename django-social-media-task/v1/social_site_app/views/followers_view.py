from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from social_site_app.models import UserProfile


@login_required(login_url='/')
def follow_profile(request, email):
    try:
        user_to_follow = get_object_or_404(UserProfile, user__email=email)
        request.user.userprofile.followers.add(user_to_follow.user)
        messages.success(request, f"Followed user: {user_to_follow.user.email}")
    except Http404:
        messages.error(request, "User Not exists")

    return redirect('users_list')


@login_required(login_url='/')
def unfollow_profile(request, email):
    try:
        user_to_unfollow = get_object_or_404(UserProfile, user__email=email)
        request.user.userprofile.followers.remove(user_to_unfollow.user)
        messages.success(request, f"Unfollowed user: {user_to_unfollow.user.email}")
    except Http404:
        messages.error(request, "User Not exists")
    return redirect('users_list')
