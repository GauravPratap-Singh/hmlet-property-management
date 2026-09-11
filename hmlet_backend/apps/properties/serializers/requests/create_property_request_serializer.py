from rest_framework import serializers
from hmlet_backend.apps.properties.models.requests.create_property_request import CreatePropertyRequest

class CreatePropertyRequestSerializer(serializers.Serializer):
    property_name = serializers.CharField(
        max_length=255, required=True, allow_null=False, allow_blank=False
    )
    address_line1 = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    address_line2 = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    postcode = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    country = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def validate(self, attrs):
        if not attrs.get("address_line1") and not attrs.get("postcode"):
            raise serializers.ValidationError(
                "Either 'address_line1' or 'postcode' must be provided."
            )
        return attrs

    def create(self, validated_data):
        return CreatePropertyRequest(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance