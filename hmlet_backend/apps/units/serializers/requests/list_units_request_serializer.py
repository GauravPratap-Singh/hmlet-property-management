from rest_framework import serializers
from hmlet_backend.apps.units.models.entities.units import Units
from hmlet_backend.apps.units.models.requests.list_units_request import ListUnitsRequest


class ListUnitsRequestSerializer(serializers.Serializer):
    status = serializers.ChoiceField(
        choices=Units.Status.choices, required=False, allow_null=True
    )

    def create(self, validated_data):
        return ListUnitsRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        return instance
