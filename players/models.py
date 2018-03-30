from django.contrib.auth.models import AbstractUser
from django.db import models

from ragnarok.models import Account


class Player(AbstractUser):

    def __str__(self):
        return self.username

    @property
    def accounts(self):
        return Account.objects.filter(username=self.username)
