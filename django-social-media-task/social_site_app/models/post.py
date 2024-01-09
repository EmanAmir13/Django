import uuid
from django.utils import timezone

from django.db import models
from django.contrib.auth import get_user_model


def generate_uuid_filename(instance, filename):
    # Get the file extension from the original filename
    img_extention = filename.split('.')[-1]
    # Generate a unique UUID
    unique_filename = f"{uuid.uuid4().hex}.{img_extention}"
    user_email = instance.user.email
    return f"post_images/{user_email}/{unique_filename}"


class UserPost(models.Model):
    """
    This model represents additional information about a user's posts,
    including an explanation and an optional image.
    The user field establishes a foreign key relationship with the built-in user model.
    """
    user = models.ForeignKey(get_user_model(), related_name='user_posts', on_delete=models.CASCADE)
    post_explanation = models.TextField(null=True)
    post_image = models.ImageField(upload_to=generate_uuid_filename, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
