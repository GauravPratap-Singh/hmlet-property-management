from django.db import models
from hmlet_backend.models.base import BaseModel
from hmlet_backend.apps.properties.models.entities.properties import Properties

class Units(BaseModel):

    """ 
    For Assignment I have used the textchoice option to implement it.
    For production, we can use table like tbl_typegroup like status and
    tbl_typevalues which will store the value like "available" and "occupied" with foriegn key from tbl_typegroup
    """
    class Status(models.TextChoices): 
        AVAILABLE = "available", "Available"
        OCCUPIED = "occupied", "Occupied"


    properties = models.ForeignKey(Properties,on_delete=models.CASCADE,related_name="units")
    unit_number = models.CharField(max_length=100)
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    status = models.CharField(max_length=20,choices=Status.choices,null=True,blank=True)

    class Meta:
        db_table = "tbl_units"
    
    def __str__(self):
        return f"{self.properties.property_name} - {self.unit_number}"