from django.contrib.auth import get_user_model
from django import forms

from django.contrib.auth.forms import UserCreationForm

from social_site_app.models.profile import UserProfile
from social_site_app.models.post import UserPost


class UserForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'mobile']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'image', 'address']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['bio'].required = True
        self.fields['address'].required = True


class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['post_explanation', 'post_image']

    # def __init__(self, *args, **kwargs):
    #     super(UserPostForm, self).__init__(*args, **kwargs)
    #     self.fields['post_image'].required = False


