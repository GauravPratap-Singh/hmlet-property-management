from rest_framework import serializers
from hmlet_backend.apps.properties.models.requests.get_property_request import GetPropertyRequest

class GetPropertyRequestSerializer(serializers.Serializer):
    property_id = serializers.IntegerField(required=True, allow_null=False, allow_blank=False)

    def create(self, validated_data):
        return GetPropertyRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.property_id = validated_data.get('property_id', instance.property_id)
        return instance