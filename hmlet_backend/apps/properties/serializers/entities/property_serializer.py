from rest_framework import serializers
from hmlet_backend.apps.properties.models.entities.properties import Properties

class PropertySerializer(serializers.Serializer):
    class Meta:
        model = Properties
        exclude = ['created_at', 'updated_at']