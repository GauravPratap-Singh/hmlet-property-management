from rest_framework import serializers
from hmlet_backend.apps.units.serializers.entities.unit_serializer import (
    UnitSerializer,
)
from hmlet_backend.apps.units.models.responses.create_unit_response import (
    CreateUnitResponse,
)


class CreateUnitResponseSerializer(serializers.Serializer):
    unit = UnitSerializer(required=False, allow_null=True)

    def create(self, validated_data):
        return CreateUnitResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.unit = validated_data.get('unit', instance.unit)
        return instance
