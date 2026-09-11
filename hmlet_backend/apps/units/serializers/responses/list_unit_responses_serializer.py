from rest_framework.serializers import Serializer
from hmlet_backend.apps.units.models.responses.list_unit_response import (
    ListUnitResponse,
)
from hmlet_backend.apps.units.serializers.entities.unit_serializer import (
    UnitSerializer,
)


class ListUnitResponseSerializer(Serializer):
    units = UnitSerializer(many=True, required=False)

    def create(self, validated_data):
        return ListUnitResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.units = validated_data.get("units", instance.units)
        return instance
