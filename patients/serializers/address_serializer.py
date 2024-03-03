from rest_framework import serializers

from patients.models import Address, Patient


class AddressSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Patient.objects.all())
    class Meta:
        model = Address
        fields = ['id', 'address1', 'address2', 'city', 'state', 'zip_code', 'country', 'patient']