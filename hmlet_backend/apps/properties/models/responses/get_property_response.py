from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.properties.models.entities.properties import Properties

class GetPropertyResponse(ABaseResponse):
    def __init__(self,
    message: str | None = None,
    property: Properties | None = None,
    reason_code: int = status.HTTP_200_OK,
    ):
        super().__init__(reason_code, message)
        self.property: Properties | None = property