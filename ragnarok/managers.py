from django.db import models


class AccountManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().exclude(account_id=1)
