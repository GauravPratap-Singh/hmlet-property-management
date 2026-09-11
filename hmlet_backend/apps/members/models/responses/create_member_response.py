from rest_framework import status
from hmlet_backend.utils.a_base_response import ABaseResponse
from hmlet_backend.apps.members.models.entities.members import Members

class CreateMemberResponse(ABaseResponse):
    def __init__(self,
        message: str | None = None,
        member: Members | None = None,
        reason_code: int = status.HTTP_201_CREATED,
    ):
        super().__init__(reason_code, message)
        self.member: Members | None = member