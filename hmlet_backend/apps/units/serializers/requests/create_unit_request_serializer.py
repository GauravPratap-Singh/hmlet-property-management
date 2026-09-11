from rest_framework import serializers
from hmlet_backend.apps.units.models.entities.units import Units
from hmlet_backend.apps.units.models.requests.create_unit_request import CreateUnitRequest


class CreateUnitRequestSerializer(serializers.Serializer):
    unit_number = serializers.CharField(
        max_length=100, required=True, allow_null=False, allow_blank=False
    )
    monthly_rent = serializers.DecimalField(
        max_digits=10, decimal_places=2, required=True, allow_null=False
    )
    status = serializers.ChoiceField(
        choices=Units.Status.choices, required=False, allow_null=True
    )

    def create(self, validated_data):
        return CreateUnitRequest(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance
