from rest_framework import serializers
from hmlet_backend.apps.members.models.entities.members import Members

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        exclude = ['created_at', 'updated_at']