from rest_framework.serializers import Serializer
from hmlet_backend.apps.members.serializers.entities.member_serializer import MemberSerializer
from hmlet_backend.apps.members.models.responses.list_member_response import ListMemberResponse

class ListMemberResponseSerializer(Serializer):
    members = MemberSerializer(many=True, required=False, allow_null=True)

    def create(self, validated_data):
        return ListMemberResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.members = validated_data.get("members", instance.members)
        return instance