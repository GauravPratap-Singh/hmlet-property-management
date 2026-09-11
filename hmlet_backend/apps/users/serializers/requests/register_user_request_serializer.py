from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from hmlet_backend.apps.users.models.requests.register_user_request import (
RegisterUserRequest,
)


class RegisterUserRequestSerializer(serializers.Serializer):

    username = serializers.CharField(
    max_length=150, required=True, allow_null=False, allow_blank=False
    )
    email = serializers.EmailField(required=True, allow_null=False)
    password = serializers.CharField(
    required=True,
    allow_null=False,
    allow_blank=False,
    write_only=True,
    style={"input_type": "password"},
    )

    def validate_password(self, value):
        try:
            validate_password(value)
        except DjangoValidationError as exc:
            raise serializers.ValidationError(list(exc.messages))
        return value

    def create(self, validated_data):
        return RegisterUserRequest(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        return instance