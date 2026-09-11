from hmlet_backend.models.base import BaseModel
from django.db import models

class Properties(BaseModel):
    property_name = models.CharField(max_length=255,null=False, blank=False)
    address_line1 = models.CharField(max_length=255, null=True,blank=True)
    address_line2 = models.CharField(max_length=255, null=True,blank=True)
    postcode = models.CharField(max_length=125, null=True,blank=True)
    country = models.CharField(max_length=125,null=True,blank=True)

    class Meta:
        db_table = "tbl_properties"

    def __str__(self):
        return self.property_name