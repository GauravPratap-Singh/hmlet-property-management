from hmlet_backend.models.base import BaseModel
from django.db import models

class Members(BaseModel):
    first_name = models.CharField(max_length=225, null=False,blank=False)
    last_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "tbl_members"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"