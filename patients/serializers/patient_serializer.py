from rest_framework import serializers

from patients.models import Patient
from patients.serializers import AddressSerializer, ConciseAdditionalFieldSerializer


class ConcisePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "full_name", "status", "city", "date_of_birth"]


class PatientSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    additional_fields = ConciseAdditionalFieldSerializer(many=True)

    class Meta:
        model = Patient
        fields = [
            "id", "first_name", "middle_name", "last_name", "status", "email", "date_of_birth", "addresses", "additional_fields"
        ]