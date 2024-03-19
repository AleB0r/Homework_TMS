from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import User
from users.forms import UserRegisterForm, LoginForm


class UserCreateView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('laptops_list')


class UserLoginView(LoginView):
    template_name = 'auth.html'
    form_class = LoginForm



class UserLogoutView(LogoutView):
    # Define the redirect URL after logout
    logout_redirect_url = reverse_lazy('login')
