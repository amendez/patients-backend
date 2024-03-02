from rest_framework import permissions, viewsets

from patients.models import Patient
from patients.serializers import ConcisePatientSerializer, PatientSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = ConcisePatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return ConcisePatientSerializer
        return PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(provider=self.request.user).prefetch_related("addresses", "additional_fields")