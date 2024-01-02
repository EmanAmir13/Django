import uuid
from django.db import models
from django.contrib.auth.models import User
import os


# def generate_filename(instance, filename):
#     _, extension = os.path.splitext(filename)
#     unique_filename = f"{uuid.uuid4()}{extension}"
#     return os.path.join('profile_images', unique_filename)
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,
#                                 related_name='profile')
#     bio = models.TextField(blank=True)
#     image = models.ImageField(upload_to=generate_filename, default='profile_images/default_user_image.png')
#     address = models.CharField(max_length=100, blank=True)

    # Specify the REQUIRED_FIELDS attribute
    # REQUIRED_FIELDS = ['username']

    # def __str__(self):
    #     return f'{self.username} Profile'
