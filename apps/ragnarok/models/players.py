from django.db import models

from model_utils import Choices

from .items import Item

from ..managers import AccountManager, CharacterManager


class Account(models.Model):
    GENDERS = Choices(('M', 'male', 'Male'), ('F', 'female', 'Female'))

    account_id = models.AutoField(primary_key=True, default=2000000)
    username = models.CharField(db_column='userid', max_length=23)
    password = models.CharField(db_column='user_pass', max_length=32)
    gender = models.CharField(
        db_column='sex', choices=GENDERS, default=GENDERS.male, max_length=1
    )
    email = models.CharField(max_length=39)
    group_id = models.IntegerField(default=0)
    state = models.PositiveIntegerField(default=0)
    unban_time = models.PositiveIntegerField(default=0)
    expiration_time = models.PositiveIntegerField(default=0)
    logincount = models.PositiveIntegerField(default=0)
    lastlogin = models.DateTimeField(blank=True, null=True)
    last_ip = models.CharField(max_length=100, default='')
    birthdate = models.DateField(blank=True, null=True)
    character_slots = models.PositiveIntegerField(default=0)

    objects = AccountManager()

    class Meta:
        db_table = 'login'
        ordering = ['account_id']

    def __str__(self):
        return self.username


class Storage(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, db_column='account_id'
    )
    item = models.ForeignKey(Item, on_delete=models.PROTECT, db_column='nameid')
    amount = models.PositiveSmallIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.PositiveSmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        db_table = 'storage'
        managed = False
        ordering = ['account_id']


class Character(models.Model):
    char_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(
        Account, on_delete=models.PROTECT, db_column='account_id'
    )
    char_num = models.IntegerField()
    name = models.CharField(unique=True, max_length=30)
    job_class = models.PositiveSmallIntegerField(db_column='class')
    base_level = models.PositiveSmallIntegerField()
    job_level = models.PositiveSmallIntegerField()
    base_exp = models.BigIntegerField()
    job_exp = models.BigIntegerField()
    zeny = models.PositiveIntegerField()
    str = models.PositiveSmallIntegerField()
    agi = models.PositiveSmallIntegerField()
    vit = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    luk = models.PositiveSmallIntegerField()
    max_hp = models.PositiveIntegerField()
    hp = models.PositiveIntegerField()
    max_sp = models.PositiveIntegerField()
    sp = models.PositiveIntegerField()
    status_point = models.PositiveIntegerField()
    skill_point = models.PositiveIntegerField()
    option = models.IntegerField()
    karma = models.IntegerField()
    manner = models.SmallIntegerField()
    party_id = models.PositiveIntegerField()
    guild_id = models.PositiveIntegerField()
    pet_id = models.PositiveIntegerField()
    homun_id = models.PositiveIntegerField()
    elemental_id = models.PositiveIntegerField()
    hair = models.PositiveIntegerField()
    hair_color = models.PositiveSmallIntegerField()
    clothes_color = models.PositiveSmallIntegerField()
    body = models.PositiveSmallIntegerField()
    weapon = models.PositiveSmallIntegerField()
    shield = models.PositiveSmallIntegerField()
    head_top = models.PositiveSmallIntegerField()
    head_mid = models.PositiveSmallIntegerField()
    head_bottom = models.PositiveSmallIntegerField()
    robe = models.PositiveSmallIntegerField()
    last_map = models.CharField(max_length=11)
    last_x = models.PositiveSmallIntegerField()
    last_y = models.PositiveSmallIntegerField()
    save_map = models.CharField(max_length=11)
    save_x = models.PositiveSmallIntegerField()
    save_y = models.PositiveSmallIntegerField()
    partner_id = models.PositiveIntegerField()
    online = models.IntegerField()
    father = models.PositiveIntegerField()
    mother = models.PositiveIntegerField()
    child = models.PositiveIntegerField()
    fame = models.PositiveIntegerField()
    rename = models.PositiveSmallIntegerField()
    delete_date = models.PositiveIntegerField()
    moves = models.PositiveIntegerField()
    unban_time = models.PositiveIntegerField()
    font = models.PositiveIntegerField()
    uniqueitem_counter = models.PositiveIntegerField()
    sex = models.CharField(max_length=1)
    hotkey_rowshift = models.PositiveIntegerField()
    clan_id = models.PositiveIntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    title_id = models.PositiveIntegerField()
    show_equip = models.PositiveIntegerField()

    objects = CharacterManager()

    class Meta:
        db_table = 'char'
        managed = False
        ordering = ['account_id']

    def __str__(self):
        return self.name


class Inventory(models.Model):
    character = models.ForeignKey(
        Character, on_delete=models.PROTECT, db_column='char_id'
    )
    item = models.ForeignKey(Item, on_delete=models.PROTECT, db_column='nameid')
    amount = models.PositiveIntegerField()
    equip = models.PositiveIntegerField()
    identify = models.SmallIntegerField()
    refine = models.PositiveIntegerField()
    attribute = models.PositiveIntegerField()
    card0 = models.PositiveSmallIntegerField()
    card1 = models.PositiveSmallIntegerField()
    card2 = models.PositiveSmallIntegerField()
    card3 = models.PositiveSmallIntegerField()
    option_id0 = models.SmallIntegerField()
    option_val0 = models.SmallIntegerField()
    option_parm0 = models.IntegerField()
    option_id1 = models.SmallIntegerField()
    option_val1 = models.SmallIntegerField()
    option_parm1 = models.IntegerField()
    option_id2 = models.SmallIntegerField()
    option_val2 = models.SmallIntegerField()
    option_parm2 = models.IntegerField()
    option_id3 = models.SmallIntegerField()
    option_val3 = models.SmallIntegerField()
    option_parm3 = models.IntegerField()
    option_id4 = models.SmallIntegerField()
    option_val4 = models.SmallIntegerField()
    option_parm4 = models.IntegerField()
    expire_time = models.PositiveIntegerField()
    favorite = models.PositiveIntegerField()
    bound = models.PositiveIntegerField()
    unique_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'inventory'
        ordering = ['character']
        verbose_name_plural = 'inventories'


class Memo(models.Model):
    memo_id = models.AutoField(primary_key=True)
    character = models.ForeignKey(
        Character, on_delete=models.PROTECT, db_column='char_id'
    )
    map = models.CharField(max_length=11)
    x = models.PositiveSmallIntegerField()
    y = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'memo'
        managed = False
        ordering = ['character']
