from django.contrib.auth.models import User
from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    middle_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=False, null=False)
    email = models.EmailField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = (
        ('Inquiry', 'Inquiry'),
        ('Onboarding', 'Onboarding'),
        ('Active', 'Active'),
        ('Churned', 'Churned'),
    )
    status = models.CharField(choices=STATUS_CHOICES, default='Inquiry')

    provider = models.ForeignKey(
        User, related_name="patients", null=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def city(self):
        return self.addresses.first().city if self.addresses.exists() else None
