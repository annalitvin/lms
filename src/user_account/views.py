from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from user_account.forms import UserAccountRegistrationForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'user_account/registration.html'
    form_class = UserAccountRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register new user'
        return context

    def get_success_url(self):
        return reverse('index')
