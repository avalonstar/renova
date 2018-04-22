from rest_framework import serializers

from .models import Item, Monster


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class MonsterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monster
        fields ='__all__'
