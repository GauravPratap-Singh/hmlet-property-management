from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from hmlet_backend.apps.users.impl.user_impl import UserImpl
from hmlet_backend.apps.users.serializers.requests.register_user_request_serializer import (
RegisterUserRequestSerializer,
)
from hmlet_backend.apps.users.serializers.requests.login_user_request_serializer import (
LoginUserRequestSerializer,
)
from hmlet_backend.apps.users.serializers.responses.register_user_responses_serializer import (
RegisterUserResponseSerializer,
)
from hmlet_backend.apps.users.serializers.responses.login_user_responses_serializer import (
LoginUserResponseSerializer,
)
from hmlet_backend.utils.a_response import AResponse

class UserView(ViewSet):
    permission_classes = [AllowAny]
    authentication_classes = []

    def register_user(self,request: Request) -> Response:
        api_resp = AResponse(message="User registered successfully")
        serializer_data = RegisterUserRequestSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        impl_resp = UserImpl.register_user(request=req)
        api_resp.set_data(RegisterUserResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)

        return api_resp.serialize()


    def login_user(self, request: Request) -> Response:
        api_resp = AResponse(message="Login successful")

        serializer_data = LoginUserRequestSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)

        impl_resp = UserImpl.login_user(request=req)
        api_resp.set_data(LoginUserResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)

        return api_resp.serialize()