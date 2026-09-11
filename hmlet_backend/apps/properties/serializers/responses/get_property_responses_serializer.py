
from rest_framework.serializers import Serializer

from hmlet_backend.apps.properties.models.responses.get_property_response import (
    GetPropertyResponse,
)
from hmlet_backend.apps.properties.serializers.entities.property_detail_serializer import (
    PropertyDetailSerializer,
)


class GetPropertyResponseSerializer(Serializer):
    property = PropertyDetailSerializer( required=False, allow_null=True)

    def create(self, validated_data):
        return GetPropertyResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.property = validated_data.get(
            "property", instance.property
        )
        return instance