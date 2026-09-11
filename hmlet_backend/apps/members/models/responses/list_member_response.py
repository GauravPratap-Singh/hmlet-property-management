from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.members.models.entities.members import Members

class ListMemberResponse(ABaseResponse):
    def __init__(self,
        message: str | None = None,
        members: list | None = None,
        reason_code: int = status.HTTP_200_OK,
    ):
        super().__init__(reason_code, message)
        self.members: list[Members] | None = members