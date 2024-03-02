from django.contrib.auth.models import User
from django.db import models


class AdditionalField(models.Model):
    provider = models.ForeignKey(
        User, related_name="additional_fields", null=True, on_delete=models.PROTECT
    )
    patient = models.ForeignKey(
        "patients.Patient", related_name="additional_fields", null=True, on_delete=models.PROTECT
    )
    additional_field = models.ForeignKey(
        "patients.AdditionalFieldConfiguration", related_name="additional_fields_values", null=True, on_delete=models.PROTECT
    )
    value = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return self.value

    @property
    def name(self):
        return self.additional_field.name