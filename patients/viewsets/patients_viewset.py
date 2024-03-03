from rest_framework import permissions, viewsets, filters

from patients.models import Patient
from patients.serializers import ConcisePatientSerializer, PatientSerializer


class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = ConcisePatientSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["first_name", "middle_name", "last_name", "date_of_birth", "status", "addresses__city"]
    ordering_fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'status']
    ordering = ['-created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return ConcisePatientSerializer
        return PatientSerializer

    def get_queryset(self):
        return Patient.objects.filter(provider=self.request.user).prefetch_related("addresses", "additional_fields")