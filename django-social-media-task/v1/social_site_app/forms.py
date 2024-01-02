from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


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
