from django.conf import settings
from django.db import models

from .items import Item

from ..utils import (MONSTER_RACE, MONSTER_SCALE)


class Monster(models.Model):
    id = models.PositiveIntegerField(db_column='ID', primary_key=True)
    sprite = models.TextField(db_column='Sprite', default='')
    kname = models.TextField(db_column='kName', default='')
    iname = models.TextField(db_column='iName', default='')

    lv = models.PositiveIntegerField(db_column='LV', default=0)
    hp = models.PositiveIntegerField(db_column='HP', default=0)
    sp = models.PositiveIntegerField(db_column='SP', default=0)
    exp = models.PositiveIntegerField(db_column='EXP', default=0)
    jexp = models.PositiveIntegerField(db_column='JEXP', default=0)
    range1 = models.PositiveIntegerField(db_column='Range1', default=0)
    range2 = models.PositiveIntegerField(db_column='Range2', default=0)
    range3 = models.PositiveIntegerField(db_column='Range3', default=0)

    atk1 = models.PositiveSmallIntegerField(db_column='ATK1', default=0)
    atk2 = models.PositiveSmallIntegerField(db_column='ATK2', default=0)
    def1 = models.PositiveSmallIntegerField(db_column='DEF', default=0)
    mdef = models.PositiveSmallIntegerField(db_column='MDEF', default=0)
    str = models.PositiveSmallIntegerField(db_column='STR', default=0)
    agi = models.PositiveSmallIntegerField(db_column='AGI', default=0)
    vit = models.PositiveSmallIntegerField(db_column='VIT', default=0)
    int = models.PositiveSmallIntegerField(db_column='INT', default=0)
    dex = models.PositiveSmallIntegerField(db_column='DEX', default=0)
    luk = models.PositiveSmallIntegerField(db_column='LUK', default=0)

    scale = models.PositiveIntegerField(
        db_column='Scale', choices=MONSTER_SCALE, default=0
    )
    race = models.PositiveIntegerField(
        db_column='Race', choices=MONSTER_RACE, default=0
    )
    element = models.PositiveIntegerField(db_column='Element', default=0)
    mode = models.PositiveIntegerField(db_column='Mode', default=0)
    speed = models.PositiveSmallIntegerField(db_column='Speed', default=0)
    adelay = models.PositiveSmallIntegerField(db_column='aDelay', default=0)
    amotion = models.PositiveSmallIntegerField(db_column='aMotion', default=0)
    dmotion = models.PositiveSmallIntegerField(db_column='dMotion', default=0)

    mexp = models.PositiveIntegerField(db_column='MEXP', default=0)
    mvp1id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='MVP1id',
        related_name='mvpdrop1',
        default=0,
    )
    mvp1per = models.PositiveSmallIntegerField(db_column='MVP1per', default=0)
    mvp2id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='MVP2id',
        related_name='mvpdrop2',
        default=0,
    )
    mvp2per = models.PositiveSmallIntegerField(db_column='MVP2per', default=0)
    mvp3id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='MVP3id',
        related_name='mvpdrop3',
        default=0,
    )
    mvp3per = models.PositiveSmallIntegerField(db_column='MVP3per', default=0)
    drop1id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop1id',
        related_name='drop1',
        default=0,
    )
    drop1per = models.PositiveSmallIntegerField(
        db_column='Drop1per', default=0
    )
    drop2id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop2id',
        related_name='drop2',
        default=0,
    )
    drop2per = models.PositiveSmallIntegerField(
        db_column='Drop2per', default=0
    )
    drop3id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop3id',
        related_name='drop3',
        default=0,
    )
    drop3per = models.PositiveSmallIntegerField(
        db_column='Drop3per', default=0
    )
    drop4id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop4id',
        related_name='drop4',
        default=0,
    )
    drop4per = models.PositiveSmallIntegerField(
        db_column='Drop4per', default=0
    )
    drop5id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop5id',
        related_name='drop5',
        default=0,
    )
    drop5per = models.PositiveSmallIntegerField(
        db_column='Drop5per', default=0
    )
    drop6id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop6id',
        related_name='drop6',
        default=0,
    )
    drop6per = models.PositiveSmallIntegerField(
        db_column='Drop6per', default=0
    )
    drop7id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop7id',
        related_name='drop7',
        default=0,
    )
    drop7per = models.PositiveSmallIntegerField(
        db_column='Drop7per', default=0
    )
    drop8id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop8id',
        related_name='drop8',
        default=0,
    )
    drop8per = models.PositiveSmallIntegerField(
        db_column='Drop8per', default=0
    )
    drop9id = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='Drop9id',
        related_name='drop9',
        default=0,
    )
    drop9per = models.PositiveSmallIntegerField(
        db_column='Drop9per', default=0
    )
    dropcardid = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        db_column='DropCardid',
        related_name='card',
        default=0,
    )
    dropcardper = models.PositiveSmallIntegerField(
        db_column='DropCardper', default=0
    )

    class Meta:
        db_table = 'mob_db_re'
        managed = settings.TESTING
        ordering = ['id']
