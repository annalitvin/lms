from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserAccountProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(default='default.jpg', upload_to='pics')
