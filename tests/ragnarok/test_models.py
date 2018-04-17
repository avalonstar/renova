import pytest

from apps.ragnarok.models import Item
from apps.ragnarok.factories import ItemFactory

pytestmark = pytest.mark.django_db


class TestItems:
    def test_factory(self):
        factory = ItemFactory()
        assert isinstance(factory, Item)

    def test_equippable_jobs(self):
        on_assassin = ItemFactory(equip_jobs=0x00001000)
        on_all = ItemFactory(equip_jobs=0xFFFFFFFF)
        on_all_no_novice = ItemFactory(equip_jobs=0xFFFFFFFE)
        assert on_assassin.equippable_jobs == ['Assassin']
        assert on_all.equippable_jobs == ['All Jobs']
        assert on_all_no_novice.equippable_jobs == ['All Jobs (Except Novice)']
