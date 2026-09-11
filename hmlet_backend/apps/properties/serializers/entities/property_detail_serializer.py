from rest_framework import serializers
from hmlet_backend.apps.properties.models.entities.properties import Properties
from hmlet_backend.apps.units.serializers.entities.unit_serializer import UnitSerializer

class PropertyDetailSerializer(serializers.Serializer):
    units = UnitSerializer(many=True, read_only=True)
    class Meta:
        model = Properties
        exclude = ['created_at', 'updated_at']
        