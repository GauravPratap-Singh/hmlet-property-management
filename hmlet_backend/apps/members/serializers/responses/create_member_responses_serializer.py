from rest_framework.serializers import Serializer
from hmlet_backend.apps.members.serializers.entities.member_serializer import MemberSerializer
from hmlet_backend.apps.members.models.responses.create_member_response import CreateMemberResponse

class CreateMemberResponseSerializer(Serializer):
    member = MemberSerializer(required=False, allow_null=True)

    def create(self, validated_data):
        return CreateMemberResponse(**validated_data)
    
    def update(self, instance, validated_data):
        instance.member = validated_data.get("member", instance.member)
        return instance