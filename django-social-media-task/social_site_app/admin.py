from django.contrib import admin
from .models import User
from .models import UserPost
from .models import UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserPost)