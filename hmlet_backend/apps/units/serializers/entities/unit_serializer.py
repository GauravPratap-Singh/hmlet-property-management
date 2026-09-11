from rest_framework import serializers
from hmlet_backend.apps.units.models.entities.units import Units

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        exclude = ['created_at', 'updated_at']