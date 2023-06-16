from rest_framework import serializers
from core.models import UserProfile, Silo, Planet


class PlanetInfoSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='owner.username')
    orion_coins = serializers.IntegerField(source='owner.profile.orion_credits')
    silo_store_resources = serializers.CharField(source='silo.stored_resources')

    class Meta:
        model = Planet
        fields = ['player_name', 'orion_coins', 'id', 'silo_store_resources']


class PlanetIdSerializer(serializers.ModelSerializer):
    """
    Serializer for Planet objects that only includes the  planet ID.
    """
    class Meta:
        model = Planet
        fields = ['id', 'name']