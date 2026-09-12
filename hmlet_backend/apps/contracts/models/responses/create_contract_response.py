from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.contracts.models.entities.contracts import Contracts

class CreateContractResponse(ABaseResponse):
    def __init__(
          self,
          message: str | None = None,
          contract: Contracts | None = None,
          reason_code: int = status.HTTP_201_CREATED,
      ):
          super().__init__(reason_code, message)
          self.contract: Contracts | None = contract