from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from hmlet_backend.apps.properties.impl.property_impl import PropertyImpl
from hmlet_backend.apps.properties.serializers.requests.create_property_request_serializer import CreatePropertyRequestSerializer
from hmlet_backend.apps.properties.serializers.requests.get_property_request_serializer import GetPropertyRequestSerializer
from hmlet_backend.apps.properties.serializers.responses.create_property_responses_serializer import CreatePropertyResponseSerializer
from hmlet_backend.apps.properties.serializers.responses.get_property_responses_serializer import GetPropertyResponseSerializer
from hmlet_backend.apps.properties.serializers.responses.list_property_responses_serializer import ListPropertyResponseSerializer
from hmlet_backend.utils.a_response import AResponse
from hmlet_backend.apps.properties.models.requests.get_property_request import (
    GetPropertyRequest,
)


class PropertyView(ViewSet):
    permission_classes = [IsAuthenticated]

    def create_property(self, request: Request) -> Response:
        api_resp = AResponse(message="Property created successfully")
        serializer_data = CreatePropertyRequestSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        req.created_by = request.user.id
        impl_resp = PropertyImpl.create_property(request=req)
        api_resp.set_data(CreatePropertyResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()

    def get_all_properties(self, request: Request) -> Response:
        api_resp = AResponse(message="Properties fetched successfully")
        impl_resp = PropertyImpl.get_all_properties()
        api_resp.set_data(ListPropertyResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()

    def get_property(self, request: Request, property_id: int = None) -> Response:
        api_resp = AResponse(message="Property fetched successfully")

        req = GetPropertyRequest(property_id=property_id)

        impl_resp = PropertyImpl.get_property(request=req)
        api_resp.set_data(GetPropertyResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)

        return api_resp.serialize()