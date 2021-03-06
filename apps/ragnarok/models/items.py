from django.conf import settings
from django.db import models

from ..utils import (
    BOOLEAN,
    EQUIPPABLE_CLASSES,
    EQUIPPABLE_GENDERS,
    EQUIPPABLE_JOBS,
    EQUIPPABLE_LOCATIONS,
    ITEM_TYPE,
)


class Item(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True, default=0)
    aegis_name = models.CharField(
        db_column='name_english', unique=True, max_length=50, default=''
    )
    name = models.CharField(
        db_column='name_japanese', max_length=50, default=''
    )
    type = models.PositiveIntegerField(default=0, choices=ITEM_TYPE)
    price_buy = models.PositiveIntegerField(blank=True, null=True)
    price_sell = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(default=0)

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
    equip_genders = models.PositiveIntegerField(
        blank=True, null=True, choices=EQUIPPABLE_GENDERS
    )
    equip_locations = models.PositiveIntegerField(blank=True, null=True)
    weapon_level = models.PositiveIntegerField(blank=True, null=True)
    equip_level = models.CharField(max_length=10, blank=True, null=True)
    refineable = models.PositiveIntegerField(
        blank=True, null=True, choices=BOOLEAN
    )

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

        if len(jobs) == len(EQUIPPABLE_JOBS):
            return ['All Jobs']

        elif len(jobs) == len(EQUIPPABLE_JOBS) - 1:
            return ['All Jobs (Except Novice)']

        return jobs

    @property
    def equippable_classes(self):
        classes = [
            name
            for bit, name in EQUIPPABLE_CLASSES.items()
            if (self.equip_classes & bit)
        ]

        if len(classes) == len(EQUIPPABLE_CLASSES):
            return ['All Classes']

        return classes

    @property
    def equippable_locations(self):
        return [
            name
            for bit, name in EQUIPPABLE_LOCATIONS.items()
            if (self.equip_locations & bit)
        ]
