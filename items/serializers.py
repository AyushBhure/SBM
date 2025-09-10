from rest_framework import serializers
from .models import Item, WeatherData

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = ['id', 'city', 'temperature', 'humidity', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']
