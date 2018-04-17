from django.db import models

from ..utils import EQUIPPABLE_JOBS


class Item(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    aegis_name = models.CharField(
        db_column='name_english', unique=True, max_length=50
    )
    name = models.CharField(db_column='name_japanese', max_length=50)
    type = models.PositiveIntegerField()
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField()

    atk_matk = models.CharField(
        db_column='atk:matk', max_length=11, blank=True, null=True
    )
    defence = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveIntegerField(blank=True, null=True)
    slots = models.PositiveIntegerField(blank=True, null=True)

    equip_jobs = models.BigIntegerField(blank=True, null=True)
    equip_classes = models.PositiveIntegerField(
        db_column='equip_upper', blank=True, null=True
    )
    equip_genders = models.PositiveIntegerField(blank=True, null=True)
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.CharField(max_length=10, blank=True, null=True)
    refineable = models.PositiveIntegerField(blank=True, null=True)

    view = models.PositiveSmallIntegerField(blank=True, null=True)
    script = models.TextField(blank=True, null=True)
    equip_script = models.TextField(blank=True, null=True)
    unequip_script = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'item_db_re'
        managed = settings.TESTING
        ordering = ['id']

    def __str__(self):
        return self.name

    @property
    def equippable_jobs(self):
        jobs = [
            name
            for bit, name in EQUIPPABLE_JOBS.items()
            if (self.equip_jobs & bit)
        ]
        return jobs
