from multiprocessing import Value
from django.db import transaction
from rest_framework import status
from hmlet_backend.apps.properties.models.requests.create_property_request import CreatePropertyRequest
from hmlet_backend.apps.properties.models.requests.get_property_request import GetPropertyRequest
from hmlet_backend.apps.properties.models.responses.create_property_response import CreatePropertyResponse
from hmlet_backend.apps.properties.models.responses.get_property_response import GetPropertyResponse
from hmlet_backend.apps.properties.models.responses.list_property_response import ListPropertyResponse
from hmlet_backend.apps.properties.serializers.requests.create_property_request_serializer import CreatePropertyRequestSerializer
from hmlet_backend.apps.properties.serializers.requests.get_property_request_serializer import GetPropertyRequestSerializer
from hmlet_backend.apps.properties.serializers.responses.create_property_responses_serializer import CreatePropertyResponsesSerializer
from hmlet_backend.apps.properties.serializers.responses.get_property_responses_serializer import GetPropertyResponseSerializer
from hmlet_backend.apps.properties.serializers.responses.list_property_responses_serializer import ListPropertyResponseSerializer
from hmlet_backend.apps.properties.models.entities.properties import Properties

class PropertyImpl:
    @staticmethod
    def create_property(request: CreatePropertyRequest) -> CreatePropertyResponse:
        response = CreatePropertyResponse(message="Property created successfully")
        with transaction.atomic():
            data_value = {
                key: value
                for key, value in request.__dict__.items()
                if value is not None
            }
            response.property = Properties.objects.create(**data_value)

        return response

    @staticmethod
    def get_all_properties() -> ListPropertyResponse:
        response = ListPropertyResponse(message="Properties fetched successfully")
        response.properties = Properties.objects.order_by("-id")
        return response

    @staticmethod
    def get_property(request: GetPropertyRequest) -> GetPropertyResponse:
        response = GetPropertyResponse(message="Property fetched successfully")
        property = (
              Properties.objects.get_active()
              .prefetch_related("units")
              .filter(id=request.property_id)
              .first()
          )

        if property is None:
            response.message = "Property not found"
            response.reason_code = status.HTTP_404_NOT_FOUND
            return response

        response.property = property
        return response