from rest_framework import serializers
from rest_framework.serializers import Serializer

from hmlet_backend.apps.users.models.responses.login_user_response import (
LoginUserResponse,
)
from hmlet_backend.apps.users.serializers.entities.user_serializer import (
UserSerializer,
)


class LoginUserResponseSerializer(Serializer):
    user = UserSerializer(required=False, allow_null=True)
    access_token = serializers.CharField(required=False, allow_null=True)
    refresh_token = serializers.CharField(required=False, allow_null=True)

    def create(self, validated_data):
        return LoginUserResponse(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get("user", instance.user)
        instance.access_token = validated_data.get(
            "access_token", instance.access_token
        )
        instance.refresh_token = validated_data.get(
            "refresh_token", instance.refresh_token
        )
        return instance