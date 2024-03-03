from django.db.models import Count
from rest_framework import permissions, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=['get'])
    def stats(self, request, *args, **kwargs):
        status_count = (Patient.objects.filter(provider=self.request.user)
                        .values('status').annotate(count=Count('status')).order_by('-count')[:5])
        city_count = (Patient.objects.filter(provider=self.request.user)
                        .values('addresses__city').annotate(count=Count('addresses__city')).order_by('-count')[:5])
        return Response({"status": status_count, "city": city_count})
