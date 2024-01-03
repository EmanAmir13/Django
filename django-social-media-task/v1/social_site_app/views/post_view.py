from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from social_site_app.models import UserPost
from v1.social_site_app.forms import UserPostForm


@login_required
def create_post(request):
    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('view_posts')
    else:
        form = UserPostForm()

    return render(request, 'v1/create_post.html', {'form': form})


@login_required
def view_posts(request):
    # Display all posts
    posts = UserPost.objects.all().order_by('-id')
    return render(request, 'v1/view_posts.html', {'posts': posts})



@login_required
def view_own_posts(request):
    # Display posts only from the logged-in user
    posts = UserPost.objects.filter(user=request.user).order_by('-id')
    return render(request, 'v1/view_own_posts.html', {'posts': posts})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(UserPost, id=post_id, user=request.user)

    if request.method == 'POST':
        form = UserPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_own_posts')
    else:
        form = UserPostForm(instance=post)

    return render(request, 'v1/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(UserPost, id=post_id, user=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('view_own_posts')

    return render(request, 'v1/delete_post.html', {'post': post})
