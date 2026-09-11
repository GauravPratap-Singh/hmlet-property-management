from django.core.exceptions import ValidationError
from django.db import models

from hmlet_backend.models.base import BaseModel
from hmlet_backend.apps.members.models.entities.members import Members
from hmlet_backend.apps.units.models.entities.units import Units


class Contracts(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name="contracts")
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, related_name="contracts")
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_value = models.DecimalField(max_digits=12, decimal_places=2, editable=False, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    logged_at = models.DateTimeField(auto_now=True)
    logged_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "tbl_contracts"
    
    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("end_date must be after start_date")

        overlapping = Contracts.objects.filter(
            unit=self.unit,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date,
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError("This unit already has a contract for overlapping dates.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def __str__(self):
          return f"{self.member.first_name} {self.member.last_name} - {self.unit.unit_number}"