from model_utils import Choices


BOOLEAN = Choices((0, 'no', 'No'), (1, 'yes', 'Yes'))

ITEM_TYPE = Choices(
    (0, 'healing', 'Healing'),
    (2, 'consumable', 'Consumable'),
    (3, 'miscellaneous', 'Miscellaneous'),
    (4, 'gear', 'Equippable Gear'),
    (5, 'weapon', 'Weapon'),
    (6, 'card', 'Card'),
    (7, 'petegg', 'Pet Egg'),
    (8, 'petequipment', 'Pet Equipment'),
    (10, 'ammo', 'Ammunition'),
    (11, 'consumabledelayed', 'Consumable (Delayed)'),
    (12, 'shadowgear', 'Shadow Equipment'),
    (18, 'consumableconfirm', 'Consumable (Requires Confirmation)'),
)

EQUIPPABLE_JOBS = {
    pow(2, 0): 'Novice',
    pow(2, 1): 'Swordman',
    pow(2, 2): 'Mage',
    pow(2, 3): 'Archer',
    pow(2, 4): 'Acolyte',
    pow(2, 5): 'Merchant',
    pow(2, 6): 'Thief',
    pow(2, 7): 'Knight',
    pow(2, 8): 'Priest',
    pow(2, 9): 'Wizard',
    pow(2, 10): 'Blacksmith',
    pow(2, 11): 'Hunter',
    pow(2, 12): 'Assassin',
    pow(2, 13): 'Unused',
    pow(2, 14): 'Crusader',
    pow(2, 15): 'Monk',
    pow(2, 16): 'Sage',
    pow(2, 17): 'Rogue',
    pow(2, 18): 'Alchemist',
    pow(2, 19): 'Bard/Dancer',
    pow(2, 20): 'Unused',
    pow(2, 21): 'Taekwon',
    pow(2, 22): 'Star Gladiator',
    pow(2, 23): 'Soul Linker',
    pow(2, 24): 'Gunslinger',
    pow(2, 25): 'Ninja',
    pow(2, 26): 'Gangsi',
    pow(2, 27): 'Death Knight',
    pow(2, 28): 'Dark Collector',
    pow(2, 29): 'Kagerou/Oboro',
    pow(2, 30): 'Rebellion',
    pow(2, 31): 'Summoner',
}

EQUIPPABLE_CLASSES = {
    pow(2, 0): 'Normal Classes',
    pow(2, 1): 'Trascendent Classes',
    pow(2, 2): 'Baby Classes',
    pow(2, 3): 'Third Classes',
    pow(2, 4): 'Transcendent Third Classes',
    pow(2, 5): 'Baby Third Classes',
}

EQUIPPABLE_GENDERS = Choices(
    (0, 'male', 'Male'), (1, 'female', 'Female'), (2, 'both', 'Both')
)

EQUIPPABLE_LOCATIONS = {
    pow(0, 1): 'None',
    pow(2, 8): 'Upper Headgear',
    pow(2, 9): 'Middle Headgear',
    pow(2, 0): 'Lower Headgear',
    pow(2, 4): 'Armor',
    pow(2, 1): 'Weapon',
    pow(2, 5): 'Shield',
    pow(2, 2): 'Garment',
    pow(2, 6): 'Footgear',
    pow(2, 3): 'Right Accessory',
    pow(2, 7): 'Left Accessory',
    pow(2, 10): 'Costume Upper Headgear',
    pow(2, 11): 'Costume Middle Headgear',
    pow(2, 12): 'Costume Lower Headgear',
    pow(2, 13): 'Costume Garment/Robe',
    pow(2, 15): 'Ammo',
    pow(2, 16): 'Shadow Armor',
    pow(2, 17): 'Shadow Weapon',
    pow(2, 18): 'Shadow Shield',
    pow(2, 19): 'Shadow Shoes',
    pow(2, 20): 'Shadow Right Accessory',
    pow(2, 21): 'Shadow Left Accessory',
}
