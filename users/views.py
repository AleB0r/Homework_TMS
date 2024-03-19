from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from users.models import User
from users.forms import UserRegisterForm, LoginForm, ChangeForm


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


class UserChangeView(LoginRequiredMixin, FormView):
    form_class = ChangeForm
    template_name = 'my_profile.html'
    model = User
    success_url = reverse_lazy("my_profile")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.user
        return kwargs

    def form_valid(self, form: ChangeForm) -> HttpResponse:
        form.save(commit=True)
        return super().form_valid(form)
