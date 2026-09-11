from django.contrib.auth import authenticate
from django.db import transaction
from django.http import response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from hmlet_backend.apps.users.models.entities.user import User
from hmlet_backend.apps.users.models.requests.register_user_request import (
RegisterUserRequest,
)
from hmlet_backend.apps.users.models.requests.login_user_request import (
LoginUserRequest,
)
from hmlet_backend.apps.users.models.responses.register_user_response import (
RegisterUserResponse,
)
from hmlet_backend.apps.users.models.responses.login_user_response import (
LoginUserResponse,
)
from hmlet_backend.utils.a_response import AResponse

class UserImpl:
    @staticmethod
    def _issue_tokens(user: User) -> tuple[str,str]:
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token), str(refresh)

    @staticmethod
    def register_user(request: RegisterUserRequest) -> RegisterUserResponse:
        response = RegisterUserResponse(message="User registered successfully")

        with transaction.atomic():
            if User.objects.filter(username__iexact=request.username).exists():
                response.message = "A user with this name already exits"
                response.reason_code = status.HTTP_409_CONFLICT
                return response

            if User.objects.filter(email__iexact=request.email).exists():
                response.message = "A user with this email already exits"
                response.reason_code = status.HTTP_409_CONFLICT
                return response
            
            user = User.objects.create_user(
                username = request.username,
                email = request.email,
                password = request.password
            )

            access_token, refresh_token = UserImpl._issue_tokens(user)

            response.user = user
            response.access_token = access_token
            response.refresh_token = refresh_token

        return response

    @staticmethod
    def login_user(request: LoginUserRequest) -> LoginUserResponse:
        response = LoginUserResponse(message="Login successful")
        user = authenticate(username=request.username,password= request.password)

        if user is None:
            response.message = "Invalid username or password"
            response.reason_code = status.HTTP_401_UNAUTHORIZED
            return response

        if not user.is_active:
            response.message = "This account is inactive"
            response.reason_code = status.HTTP_403_FORBIDDEN
            return response

        access_token, refresh_token = UserImpl._issue_tokens(user)

        response.user = user
        response.access_token = access_token
        response.refresh_token = refresh_token

        return response
