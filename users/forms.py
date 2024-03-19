from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User