from rest_framework import serializers
from hmlet_backend.apps.members.models.requests.create_member_request import CreateMemberRequest

class CreateMemberRequestSerializer(serializers.Serializer):
      first_name = serializers.CharField(
          max_length=225, required=True, allow_null=False, allow_blank=False
      )
      last_name = serializers.CharField(
          max_length=255, required=False, allow_null=True, allow_blank=True
      )
      email = serializers.EmailField(required=True, allow_null=False)

      def create(self, validated_data):
          return CreateMemberRequest(**validated_data)

      def update(self, instance, validated_data):
          for attr, value in validated_data.items():
              setattr(instance, attr, value)
          return instance