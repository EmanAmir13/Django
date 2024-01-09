from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from social_site_app.models.profile import UserProfile
from v1.social_site_app.forms import UserProfileForm


@login_required(login_url='/')
def users_list(request):
    users = get_user_model().objects.exclude(id=request.user.id)
    following_ids = request.user.userprofile.followers.values_list('id', flat=True)
    return render(request, 'v1/users_list.html', {'users': users, 'following_ids': following_ids})


@login_required(login_url='/')
def create_profile(request):
    existing_profile = UserProfile.objects.filter(user=request.user).first()

    if existing_profile:
        messages.warning(request, 'Profile already exists. Edit your profile instead.')
        return redirect('edit_profile')

    if not request.method == 'POST':
        form = UserProfileForm()
        return render(request, 'v1/create_profile.html', {'form': form})

    form = UserProfileForm(request.POST, request.FILES)
    if not form.is_valid():
        messages.error(request, 'Error in the form. Please check and try again.')
    else:
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        messages.success(request, 'Profile created successfully.')
        return redirect('view_profile')

    return render(request, 'v1/create_profile.html', {'form': form})


@login_required(login_url='/')
def view_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'v1/view_profile.html', {'profile': profile})


@login_required(login_url='/')
def edit_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if not request.method == 'POST':
        form = UserProfileForm(instance=profile)
        return render(request, 'v1/edit_profile.html', {'form': form})

    form = UserProfileForm(request.POST, request.FILES, instance=profile)

    if not form.is_valid():
        return render(request, 'v1/edit_profile.html', {'form': form})

    form.save()
    followers_ids = request.POST.getlist('followers')

    profile.followers.set(followers_ids)
    if created:
        messages.success(request, 'Profile created successfully.')
    else:
        messages.success(request, 'Profile updated successfully.')
    return redirect('view_profile')


@login_required(login_url='/')
def view_other_profile(request, email):
    if not request.user.is_authenticated and request.user.email == email:
        try:
            user = get_object_or_404(get_user_model(), email=email)
            user_profile = get_object_or_404(UserProfile, user=user)
        except Http404:
            messages.error(request, "Profile Not exists")
            return render(request, 'v1/other_user_profile.html', {'user_profile': user_profile})

    user_profile = UserProfile.objects.get(user=request.user)

    return render(request, 'v1/other_user_profile.html', {'user_profile': user_profile})
