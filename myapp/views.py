from rest_framework import viewsets
from .models import Admin, UserType, Patient, Disease, VisitSchedule
from .serializers import AdminSerializer, UserSerializer, PatientSerializer, DiseaseSerializer, VisitScheduleSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class UserTypeViewSet(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer

class VisitScheduleViewSet(viewsets.ModelViewSet):
    queryset = VisitSchedule.objects.all()
    serializer_class = VisitScheduleSerializer
