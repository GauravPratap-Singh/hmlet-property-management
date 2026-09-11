from rest_framework.serializers import Serializer

from hmlet_backend.apps.properties.models.responses.list_property_response import (
    ListPropertyResponse,
)
from hmlet_backend.apps.properties.serializers.entities.property_serializer import (
    PropertySerializer,
)


class ListPropertyResponseSerializer(Serializer):
    properties = PropertySerializer(many=True, required=False)

    def create(self, validated_data):
        return ListPropertyResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.properties = validated_data.get("properties", instance.properties)
        return instance