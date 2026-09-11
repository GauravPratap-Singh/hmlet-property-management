from rest_framework import serializers
from hmlet_backend.apps.users.models.entities.user import User

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        ]
        read_only_fields = fields