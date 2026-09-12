from rest_framework import serializers
from hmlet_backend.apps.contracts.models.entities.contracts import Contracts


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        exclude = ['created_at', 'updated_at']
