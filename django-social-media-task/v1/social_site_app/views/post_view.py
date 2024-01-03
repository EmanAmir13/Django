from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from social_site_app.models.profile import UserProfile
from v1.social_site_app.forms import UserProfileForm


@login_required(login_url='/')
def create_post(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Profile created successfully.')
            return redirect('view_profile')
    else:
        form = UserProfileForm()

    return render(request, 'v1/create_profile.html', {'form': form})


@login_required(login_url='/')
def view_post(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    return render(request, 'v1/view_profile.html', {'profile': profile})


@login_required(login_url='/')
def edit_post(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            if created:
                messages.success(request, 'Profile created successfully.')
            else:
                messages.success(request, 'Profile updated successfully.')
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'v1/edit_profile.html', {'form': form})


@login_required(login_url='/')
def delete_post(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully.')
        return redirect('welcome')

    return render(request, 'v1/delete_profile.html', {'profile': profile})
