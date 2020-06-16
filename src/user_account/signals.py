from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from user_account.models import UserAccountProfile


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        UserAccountProfile.objects.create(user=instance)
    # else:
          #получается ошибка уникальности
    #     profile = getattr(instance, 'profile', UserAccountProfile.objects.create(user=instance))
    #     profile.save()
