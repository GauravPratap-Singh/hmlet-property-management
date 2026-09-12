from rest_framework.serializers import Serializer
from hmlet_backend.apps.contracts.models.responses.get_contract_response import (
    GetContractResponse,
)
from hmlet_backend.apps.contracts.serializers.entities.contract_serializer import (
    ContractSerializer,
)


class GetContractResponseSerializer(Serializer):
    contracts = ContractSerializer(many=True, required=False)

    def create(self, validated_data):
        return GetContractResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.contracts = validated_data.get("contracts", instance.contracts)
        return instance