from django.db import models
from django.dispatch import receiver

from allauth.socialaccount import signals


@receiver(signals.social_account_added)
def added_socialaccount(request, sociallogin, **kwargs):
    a = {}
    a.update(**kwargs)
    return print(request, sociallogin, a)


@receiver(signals.social_account_updated)
def updated_socialaccount(request, sociallogin, **kwargs):
    a = {}
    a.update(**kwargs)
    return print(request, sociallogin, a)
