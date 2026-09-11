from rest_framework import serializers  
from hmlet_backend.apps.properties.serializers.entities.property_serializer import (
      PropertySerializer,
  )
from hmlet_backend.apps.properties.models.responses.create_property_response import CreatePropertyResponse


class CreatePropertyResponseSerializer(serializers.Serializer):
    property = PropertySerializer(required=False, allow_null=True)

    def create(self, validated_data):
        return CreatePropertyResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.property = validated_data.get('property', instance.property)
        return instance