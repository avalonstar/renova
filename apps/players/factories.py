import factory

from . import models


class PlayerFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda i: 'player#%s' % i)
    password = 'poring'

    class Meta:
        model = models.Player
