from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm, UserProfileUpdateForm


class CreateUserAccountView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user_account/registration.html'
    form_class = UserAccountRegistrationForm

    success_message = "Registration completed successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register new user'
        return context

    def get_success_url(self):
        return reverse('index')


class UserAccountLoginView(LoginView):
    template_name = 'user_account/login.html'
    extra_context = {'title': 'Login as a user'}


class UserAccountLogoutView(LogoutView):
    template_name = 'user_account/logout.html'
    extra_context = {'title': 'Logout from LMS'}


@login_required
def user_account_update_profile(request):
    if request.method == 'POST':
        u_form = UserAccountProfileForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES,
                                       instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('account:profile')

    else:
        u_form = UserAccountProfileForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': f'Edit {request.user.get_full_name()} user profile'
    }

    return render(
        request=request,
        template_name='user_account/profile.html',
        context=context
    )
