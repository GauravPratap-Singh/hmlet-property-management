from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from hmlet_backend.apps.contracts.impl.contract_impl import ContractImpl
from hmlet_backend.apps.contracts.serializers.requests.create_contract_request_serializer import (
    CreateContractRequestSerializer,
)
from hmlet_backend.apps.contracts.serializers.requests.get_contract_request_serializer import (
    GetContractRequestSerializer,
)
from hmlet_backend.apps.contracts.serializers.responses.create_contract_responses_serializer import (
    CreateContractResponseSerializer,
)
from hmlet_backend.apps.contracts.serializers.responses.get_contract_responses_serializer import (
    GetContractResponseSerializer,
)
from hmlet_backend.utils.a_response import AResponse


class ContractView(ViewSet):
    permission_classes = [IsAuthenticated]

    def create_contract(self, request: Request) -> Response:
        api_resp = AResponse(message="Contract created successfully")
        serializer_data = CreateContractRequestSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        req.created_by = request.user.id
        impl_resp = ContractImpl.create_contract(request=req)
        api_resp.set_data(CreateContractResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()

    def get_all_contracts(self, request: Request) -> Response:
        api_resp = AResponse(message="Contracts fetched successfully")
        serializer_data = GetContractRequestSerializer(data=request.query_params)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        impl_resp = ContractImpl.get_all_contracts(request=req)
        api_resp.set_data(GetContractResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()
