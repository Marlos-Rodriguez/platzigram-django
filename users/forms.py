"""User Forms"""

# Django
from django import forms
from django.contrib.auth.models import User

from users.models import Profile


class SignupForm(forms.Form):
    """User Signup Form"""

    username = forms.CharField(
        label=False,
        min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Username',
                   'class': 'form-control', 'required': True}
        )
    )
    password = forms.CharField(
        label=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password',
                   'class': 'form-control', 'required': True}
        ))
    password_confirmation = forms.CharField(
        label=False,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password Confirmation',
                   'class': 'form-control', 'required': True}
        ))

    first_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Password Confirmation',
                   'class': 'form-control', 'required': True}
        ))

    last_name = forms.CharField(
        label=False,
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder': 'Password Confirmation',
                   'class': 'form-control', 'required': True}
        ))

    email = forms.CharField(
        label=False,
        min_length=6,
        max_length=70,
        widget=forms.EmailInput(
            attrs={'placeholder': 'Password Confirmation',
                   'class': 'form-control', 'required': True}
        )
    )

    def clean_username(self):
        """Username Must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify passowrd confirmation"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')

        return data

    def save(self):
        """Create User and Profile"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)

        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile Form"""
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
