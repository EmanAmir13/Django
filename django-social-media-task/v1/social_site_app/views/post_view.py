from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from social_site_app.models import UserPost
from v1.social_site_app.forms import UserPostForm
from django.http import Http404
from django.contrib import messages


@login_required
def create_post(request):
    if not request.method == 'POST':
        form = UserPostForm()
    form = UserPostForm(request.POST, request.FILES)
    if not form.is_valid():
        return render(request, 'v1/create_post.html', {'form': form})
    post = form.save(commit=False)
    post.user = request.user
    post.save()
    messages.success(request, "Post created successfully.")
    return redirect('view_own_posts')


@login_required
def view_posts(request):
    following_users = request.user.userprofile.followers.all()
    posts = UserPost.objects.filter(user__in=following_users).order_by('created', 'modified')

    return render(request, 'v1/view_posts.html', {'posts': posts})


@login_required
def view_own_posts(request):
    posts = UserPost.objects.filter(user=request.user).order_by('-created', '-modified')
    return render(request, 'v1/view_own_posts.html', {'posts': posts})


@login_required
def edit_post(request, post_id):
    try:
        post = get_object_or_404(UserPost, id=post_id, user=request.user)
    except Http404:
        messages.error(request, "Post not found.")
        return redirect('view_own_posts')

    if not request.method == 'POST':
        form = UserPostForm(instance=post)
    form = UserPostForm(request.POST, request.FILES, instance=post)
    if not form.is_valid():
        return render(request, 'v1/edit_post.html', {'form': form, 'post': post})
    form.save()
    messages.success(request, "Post edited successfully.")
    return redirect('view_own_posts')


@login_required
def delete_post(request, post_id):
    try:
        post = get_object_or_404(UserPost, id=post_id, user=request.user)
    except Http404:
        messages.error(request, "Post not found.")
        return redirect('view_own_posts')

    if not request.method == 'POST':
        return render(request, 'v1/delete_post.html', {'post': post})
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('view_own_posts')
