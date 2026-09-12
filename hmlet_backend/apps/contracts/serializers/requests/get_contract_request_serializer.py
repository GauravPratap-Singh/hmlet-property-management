from rest_framework import serializers
from hmlet_backend.apps.contracts.models.requests.get_contract_request import (
    GetContractRequest,
)


class GetContractRequestSerializer(serializers.Serializer):
    active = serializers.BooleanField(required=False, allow_null=True)

    def create(self, validated_data):
        return GetContractRequest(**validated_data)

    def update(self, instance, validated_data):
        instance.active = validated_data.get('active', instance.active)
        return instance