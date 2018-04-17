from django.db import models


class AccountManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().exclude(account_id=1).exclude(
            group_id=99
        )


class CharacterManager(models.Manager):

    def online(self):
        return self.filter(online=1)
