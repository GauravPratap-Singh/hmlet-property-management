from rest_framework import serializers
from hmlet_backend.apps.contracts.serializers.entities.contract_serializer import (
    ContractSerializer,
)
from hmlet_backend.apps.contracts.models.responses.create_contract_response import (
    CreateContractResponse,
)


class CreateContractResponseSerializer(serializers.Serializer):
    contract = ContractSerializer(required=False, allow_null=True)

    def create(self, validated_data):
        return CreateContractResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.contract = validated_data.get('contract', instance.contract)
        return instance