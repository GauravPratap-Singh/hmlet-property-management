from django.db import transaction
from django.http import response
from rest_framework import status
from hmlet_backend.apps.members.models.entities.members import Members
from hmlet_backend.apps.members.models.requests.create_member_request import (
    CreateMemberRequest,
)
from hmlet_backend.apps.members.models.responses.create_member_response import (
    CreateMemberResponse,
)
from hmlet_backend.apps.members.models.responses.list_member_response import (
    ListMemberResponse,
)

class MemberImpl:
    @staticmethod
    def create_member(request: CreateMemberRequest) -> CreateMemberResponse:
        response = CreateMemberResponse(message="Member created successfully")
        with transaction.atomic():
      # email is unique on the model - fail cleanly instead of a 500 on IntegrityError
            if Members.objects.filter(email__iexact=request.email).exists():
                response.message = "A member with this email already exists"
                response.reason_code = status.HTTP_409_CONFLICT
                return response

            data_value = {
                key: value
                for key, value in request.__dict__.items()
                if value is not None
            }
            response.member = Members.objects.create(**data_value)

        return response

    @staticmethod
    def get_all_members() -> ListMemberResponse:
        response = ListMemberResponse(message="Member fetched successfully")
        response.members = Members.objects.get_active().order_by("-id")
        return response