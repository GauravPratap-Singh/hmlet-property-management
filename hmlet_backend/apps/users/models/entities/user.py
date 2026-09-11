from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        db_table = "tbl_users"

    def save(self,*args,**kwargs):
        self.is_staff = True
        super().save(*args, **kwargs)