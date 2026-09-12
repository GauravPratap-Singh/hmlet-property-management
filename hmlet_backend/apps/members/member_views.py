from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from hmlet_backend.apps.members.impl.members_impl import MemberImpl
from hmlet_backend.apps.members.serializers.requests.create_member_request_serializer import (
CreateMemberRequestSerializer,
)
from hmlet_backend.apps.members.serializers.responses.create_member_responses_serializer import (
CreateMemberResponseSerializer,
)
from hmlet_backend.apps.members.serializers.responses.list_member_responses_serializer import (
ListMemberResponseSerializer,
)
from hmlet_backend.utils.a_response import AResponse

class MemberView(ViewSet):
    permission_classes = [IsAuthenticated]

    def get_all_members(self, request: Request) -> Response:
        api_resp = AResponse(message="Members fetched successfully")
        impl_resp = MemberImpl.get_all_members()
        api_resp.set_data(ListMemberResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()

    def create_member(self, request: Request) -> Response:
        api_resp = AResponse(message="Member created successfully")
        serializer_data = CreateMemberRequestSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        req = serializer_data.create(validated_data=serializer_data.validated_data)
        req.created_by = request.user.id
        impl_resp = MemberImpl.create_member(request=req)
        api_resp.set_data(CreateMemberResponseSerializer(instance=impl_resp))
        api_resp.set_message(impl_resp.message)
        api_resp.set_reason_code(impl_resp.reason_code)
        return api_resp.serialize()