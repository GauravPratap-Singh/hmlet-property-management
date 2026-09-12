from rest_framework import serializers
from hmlet_backend.apps.contracts.models.requests.create_contract_request import CreateContractRequest

class CreateContractRequestSerializer(serializers.Serializer):
      member_id = serializers.IntegerField(required=True, allow_null=False)
      unit_id = serializers.IntegerField(required=True, allow_null=False)
      start_date = serializers.DateField(required=True, allow_null=False)
      end_date = serializers.DateField(required=True, allow_null=False)
      monthly_rent = serializers.DecimalField(
          max_digits=10, decimal_places=2, required=False, allow_null=True
      )

      def validate(self, attrs):
          if attrs["end_date"] <= attrs["start_date"]:
              raise serializers.ValidationError("end_date must be after start_date.")
          return attrs

      def create(self, validated_data):
          return CreateContractRequest(**validated_data)

      def update(self, instance, validated_data):
          for attr, value in validated_data.items():
              setattr(instance, attr, value)
          return instance