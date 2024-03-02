from django.db import transaction
from rest_framework import serializers

from patients.models import Patient
from patients.serializers import AddressSerializer, ConciseAdditionalFieldSerializer


class ConcisePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "full_name", "status", "city", "date_of_birth"]


class PatientSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    additional_fields = ConciseAdditionalFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = [
            "id", "first_name", "middle_name", "last_name", "status", "email", "date_of_birth", "created_at",
            "addresses", "additional_fields"
        ]

    def create(self, validated_data):
        validated_data['provider'] = self.context['request'].user
        with transaction.atomic():
            patient = super().create(validated_data)
            for field in patient.provider.additional_field_configurations.all():
                value = self.context['request'].data.get(f"custom-{field.id}", None)
                if value:
                    patient.additional_fields.create(
                        additional_field=field, value=value, patient=patient, provider=patient.provider
                    )
            return patient
