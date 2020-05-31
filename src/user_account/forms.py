from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserAccountRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_email(self):

        email = self.cleaned_data['email']

        if User.objects.all().filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
