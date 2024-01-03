from django.contrib.auth import get_user_model
from django import forms

from django.contrib.auth.forms import UserCreationForm

from social_site_app.models.profile import UserProfile
from social_site_app.models.post import UserPost


class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'mobile']

        def save(self, commit=True):
            user = super().save(commit=False)
            user.mobile = self.cleaned_data.get('mobile')
            if commit:
                user.save()
            return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'image', 'address']


class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['post_explanation', 'post_image']
