from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    address1 = models.CharField(max_length=1024, blank=False, null=False)
    address2 = models.CharField(max_length=1024, blank=True, null=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=120,blank=False, null=False)
    state = models.CharField(max_length=120, blank=False, null=False)
    country = models.CharField(max_length=120, blank=False, null=False)

    patient = models.ForeignKey(
        "patients.Patient", related_name="addresses", null=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.address1}, {self.city}, {self.state}"