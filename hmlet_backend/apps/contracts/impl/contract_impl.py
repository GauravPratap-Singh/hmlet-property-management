from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction
from django.utils import timezone
from rest_framework import status

from hmlet_backend.apps.contracts.models.entities.contracts import Contracts
from hmlet_backend.apps.contracts.models.requests.create_contract_request import (
    CreateContractRequest,
)
from hmlet_backend.apps.contracts.models.requests.get_contract_request import (
    GetContractRequest,
)
from hmlet_backend.apps.contracts.models.responses.create_contract_response import (
    CreateContractResponse,
)
from hmlet_backend.apps.contracts.models.responses.get_contract_response import (
    GetContractResponse,
)
from hmlet_backend.apps.members.models.entities.members import Members
from hmlet_backend.apps.units.models.entities.units import Units


class ContractImpl:
    @staticmethod
    def _calculate_total_months(start_date, end_date) -> int:
        # Inclusive month count: Jan 1 -> Dec 31 of the same year spans 12 full months.
        months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        if end_date.day >= start_date.day:
            months += 1
        return max(months, 1)

    @staticmethod
    def create_contract(request: CreateContractRequest) -> CreateContractResponse:
        response = CreateContractResponse(message="Contract created successfully")

        member = Members.objects.get_active().filter(id=request.member_id).first()
        if member is None:
            response.message = "Member not found"
            response.reason_code = status.HTTP_404_NOT_FOUND
            return response

        unit = Units.objects.get_active().filter(id=request.unit_id).first()
        if unit is None:
            response.message = "Unit not found"
            response.reason_code = status.HTTP_404_NOT_FOUND
            return response

        overlapping = Contracts.objects.get_active().filter(
            unit_id=unit.id,
            start_date__lte=request.end_date,
            end_date__gte=request.start_date,
        ).exists()
        if overlapping:
            response.message = "This unit already has a contract for overlapping dates"
            response.reason_code = status.HTTP_409_CONFLICT
            return response

        monthly_rent = (
            request.monthly_rent if request.monthly_rent is not None else unit.monthly_rent
        )
        total_value = monthly_rent * ContractImpl._calculate_total_months(
            request.start_date, request.end_date
        )

        try:
            with transaction.atomic():
                contract = Contracts.objects.create(
                    member_id=member.id,
                    unit_id=unit.id,
                    start_date=request.start_date,
                    end_date=request.end_date,
                    monthly_rent=monthly_rent,
                    total_value=total_value,
                    created_by=request.created_by,
                )
                unit.status = Units.Status.OCCUPIED
                unit.save(update_fields=["status"])
        except DjangoValidationError as exc:
            # Safety net: Contracts.save() re-runs full_clean(), which re-checks
            # overlap/date-order under the transaction in case of a race.
            response.message = "; ".join(exc.messages)
            response.reason_code = status.HTTP_400_BAD_REQUEST
            return response
            
        response.contract = contract
        return response

    @staticmethod
    def get_all_contracts(request: GetContractRequest) -> GetContractResponse:
        response = GetContractResponse(message="Contracts fetched successfully")
        contracts = Contracts.objects.get_active().order_by("-id")

        if request.active:
            today = timezone.localdate()
            contracts = contracts.filter(start_date__lte=today, end_date__gte=today)

        response.contracts = contracts
        return response