from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.properties.models.entities.properties import Properties

class ListPropertyResponse(ABaseResponse):
    def __init_(self,
          message: str,
          properties: list | None = None,
          reason_code: int = status.HTTP_200_OK,
    ):
        super().__init_(reason_code, message)
        self.properties: list[Properties] | None = properties
        