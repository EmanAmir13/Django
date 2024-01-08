import uuid
from django.db import models
from django.contrib.auth import get_user_model


def generate_uuid_filename(instance, filename):
    # Get the file extension from the original filename
    img_extention = filename.split('.')[-1]
    # Generate a unique UUID
    unique_filename = f"{uuid.uuid4().hex}.{img_extention}"
    return f"profile_images/{unique_filename}"


class UserProfile(models.Model):
    """
       This model represents additional information about a user, such as bio,
       profile image, and address. The user field establishes a one-to-one
       relationship with the built-in user model.
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    followers = models.ManyToManyField(get_user_model(), related_name='following', blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=generate_uuid_filename, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.email
