from django.db import models

class ActiveRecord(models.Manager):
    def get_active(self):
        return super().get_queryset().filter(is_active=True)

class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True)
    update_by = models.IntegerField(null=True, blank=True)

    objects = ActiveRecord()

    all_objects = models.Manager()

    class Meta:
        abstract = True