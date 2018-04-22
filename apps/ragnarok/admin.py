from django.contrib import admin

from .models import Account, Character, Item, Inventory, Monster, Storage

admin.site.register(Account)
admin.site.register(Character)
admin.site.register(Inventory)
admin.site.register(Item)
admin.site.register(Monster)
admin.site.register(Storage)
