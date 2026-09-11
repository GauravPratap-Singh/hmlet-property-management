from rest_framework import status
from hmlet_backend.apps.users.models.entities.user import User
from hmlet_backend.utils.a_base_response import ABaseResponse

class LoginUserResponse(ABaseResponse):
    def __init__(
        self,
        message: str | None = None,
        user: User | None = None,
        access_token: str | None = None,
        refresh_token: str | None = None,
        reason_code: int = status.HTTP_200_OK,
        ):
        super().__init__(reason_code, message)
        self.user: User | None = user
        self.access_token: str | None = access_token
        self.refresh_token: str | None = refresh_token