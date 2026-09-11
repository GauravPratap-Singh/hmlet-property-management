from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from hmlet_backend.apps.units.impl.unit_impl import UnitImpl
from hmlet_backend.apps.units.serializers.requests.create_unit_request_serializer import (
    CreateUnitRequestSerializer,
)
from hmlet_backend.apps.units.serializers.requests.list_units_request_serializer import (
    ListUnitsRequestSerializer,
)
from hmlet_backend.apps.units.serializers.responses.create_unit_responses_serializer import (
    CreateUnitResponseSerializer,
)
from hmlet_backend.apps.units.serializers.responses.list_unit_responses_serializer import (
    ListUnitResponseSerializer,
)
from hmlet_backend.utils.a_response import AResponse


class UnitView(ViewSet):
    permission_classes = [IsAuthenticated]

    def create_unit(self, request: Request, property_id: int = None) -> Response:
        api_resp = AResponse(message="Unit created successfully")
        serializer_data = CreateUnitRequestSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        req.properties_id = property_id
        req.created_by = request.user.id
        impl_resp = UnitImpl.create_unit(request=req)
        api_resp.set_data(CreateUnitResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()

    def get_all_units(self, request: Request) -> Response:
        api_resp = AResponse(message="Units fetched successfully")
        serializer_data = ListUnitsRequestSerializer(data=request.query_params)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        impl_resp = UnitImpl.get_all_units(request=req)
        api_resp.set_data(ListUnitResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()
