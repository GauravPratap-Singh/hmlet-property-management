from django.db import transaction
from rest_framework import status
from hmlet_backend.apps.properties.models.entities.properties import Properties
from hmlet_backend.apps.units.models.entities.units import Units
from hmlet_backend.apps.units.models.requests.create_unit_request import CreateUnitRequest
from hmlet_backend.apps.units.models.requests.list_units_request import ListUnitsRequest
from hmlet_backend.apps.units.models.responses.create_unit_response import CreateUnitResponse
from hmlet_backend.apps.units.models.responses.list_unit_response import ListUnitResponse


class UnitImpl:
    @staticmethod
    def create_unit(request: CreateUnitRequest) -> CreateUnitResponse:
        response = CreateUnitResponse(message="Unit created successfully")

        if not Properties.objects.get_active().filter(id=request.properties_id).exists():
            response.message = "Property not found"
            response.reason_code = status.HTTP_404_NOT_FOUND
            return response

        with transaction.atomic():
            data_value = {
                key: value
                for key, value in request.__dict__.items()
                if value is not None
            }
            data_value.setdefault("status", Units.Status.AVAILABLE)
            response.unit = Units.objects.create(**data_value)

        return response

    @staticmethod
    def get_all_units(request: ListUnitsRequest) -> ListUnitResponse:
        response = ListUnitResponse(message="Units fetched successfully")
        units = Units.objects.get_active().order_by("-id")

        if request.status:
            units = units.filter(status=request.status)

        response.units = units
        return response
