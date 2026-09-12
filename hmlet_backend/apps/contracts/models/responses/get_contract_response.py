from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.contracts.models.entities.contracts import Contracts


class GetContractResponse(ABaseResponse):
    def __init__(
        self,
        message: str | None = None,
        contracts: list | None = None,
        reason_code: int = status.HTTP_200_OK,
    ):
        super().__init__(reason_code, message)
        self.contracts: list[Contracts] | None = contracts