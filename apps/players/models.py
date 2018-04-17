from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.functional import cached_property

from apps.ragnarok.models import Account, Character, Storage


class Player(AbstractUser):
    account_ids = ArrayField(
        models.IntegerField(), blank=True, default=list, size=2
    )

    def __str__(self):
        return self.username

    @cached_property
    def accounts(self):
        return Account.objects.filter(account_id__in=self.account_ids)

    @cached_property
    def characters(self):
        return Character.objects.filter(account_id__in=self.account_ids)

    @property
    def has_account(self):
        return self.accounts.exists()

    @cached_property
    def storage(self):
        return Storage.objects.filter(account_id__in=self.account_ids)
