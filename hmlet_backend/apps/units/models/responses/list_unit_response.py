from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.units.models.entities.units import Units


class ListUnitResponse(ABaseResponse):
    def __init__(
        self,
        message: str | None = None,
        units: list | None = None,
        reason_code: int = status.HTTP_200_OK,
    ):
        super().__init__(reason_code, message)
        self.units: list[Units] | None = units
