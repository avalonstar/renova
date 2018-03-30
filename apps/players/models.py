from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.functional import cached_property

from apps.ragnarok.models import Account


class Player(AbstractUser):

    def __str__(self):
        return self.username

    @cached_property
    def accounts(self):
        return Account.objects.filter(username=self.username)
