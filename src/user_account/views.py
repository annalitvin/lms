from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'user_account/registration.html'
    form_class = UserAccountRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register new user'
        return context

    def get_success_url(self):
        return reverse('account:success')


class SuccessView(TemplateView):
    template_name = 'user_account/success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Success'
        return context


class UserAccountLoginView(LoginView):
    template_name = 'user_account/login.html'
    extra_context = {'title': 'Login as a user'}


class UserAccountLogoutView(LogoutView):
    template_name = 'user_account/logout.html'
    extra_context = {'title': 'Logout from LMS'}


class UserAccountProfileView(UpdateView):
    template_name = 'user_account/profile.html'
    extra_context = {'title': 'Edit current user profile'}
    form_class = UserAccountProfileForm

    def get_object(self, queryset=None):
        return self.request.user
