# # social_site_app/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# # from social_site_app.models import Profile
# from v1.social_site_app.forms import ProfileForm
#
#
# @login_required(login_url="/")
# def view_profile(request, user_id=None):
#     if user_id is not None:
#         profile = get_object_or_404(Profile, user_id=user_id)
#     else:
#         profile = request.user.profile
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             user = profile.user
#             return redirect('view_profile', user_id=user.id)
#     else:
#         form = ProfileForm(instance=profile)
#
#     context = {'profile': profile, 'form': form}
#     return render(request, "v1/user_profile.html", context=context)
#
#
# @login_required(login_url="/")
# def update_profile(request, id):
#     profile = Profile.objects.get(id=id)
#
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()
#             user = profile.user
#             return redirect('view_profile', user_id=user.id)
#
#     else:
#         form = ProfileForm(instance=profile)
#
#     context = {'profile': profile, 'form': form}
#     return render(request, "v1/update_user_profile.html", context=context)
