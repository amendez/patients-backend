from django.contrib import admin

from patients.models import Address, AdditionalField, AdditionalFieldConfiguration, Patient

admin.site.register(Patient)
admin.site.register(Address)
admin.site.register(AdditionalField)
admin.site.register(AdditionalFieldConfiguration)