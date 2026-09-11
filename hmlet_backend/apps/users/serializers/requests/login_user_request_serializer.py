from rest_framework import serializers

from hmlet_backend.apps.users.models.requests.login_user_request import (
LoginUserRequest,
)


class LoginUserRequestSerializer(serializers.Serializer):
    username = serializers.CharField(
    required=True, allow_null=False, allow_blank=False
    )
    password = serializers.CharField(
    required=True,
    allow_null=False,
    allow_blank=False,
    write_only=True,
    style={"input_type": "password"},
    )

    def create(self, validated_data):
        return LoginUserRequest(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance