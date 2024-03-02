from django.contrib.auth.models import User
from django.db import models


class AdditionalFieldConfiguration(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    TYPE_CHOICES = (
        ('Text', 'Text'),
        ('Number', 'Number'),
    )
    type = models.CharField(choices=TYPE_CHOICES, default='Text', max_length=120)

    provider = models.ForeignKey(
        User, related_name="additional_field_configurations", null=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.name}:{self.type} ({self.provider.username})"
