import factory

from . import models


class ItemFactory(factory.DjangoModelFactory):
    id = factory.Sequence(lambda i: i)
    aegis_name = factory.Sequence(lambda i: 'Test_Item_%s' % i)
    name = factory.Sequence(lambda i: 'Test Item %s' % i)

    class Meta:
        model = models.Item


class MonsterFactory(factory.DjangoModelFactory):
    id = factory.Sequence(lambda i: i)

    class Meta:
        model = models.Monster
