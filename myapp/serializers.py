from rest_framework import serializers
from .models import Admin, UserType, Patient, Disease, VisitSchedule

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['user_id', 'first_name', 'last_name', 'gender', 'mobile_phone', 'home_phone', 'address', 'national_code', 'birth_date']

class AdminSerializer(UserSerializer):
    class Meta:
        model = Admin
        fields = UserSerializer.Meta.fields + ['password']

class PatientSerializer(UserSerializer):
    class Meta:
        model = Patient
        fields = UserSerializer.Meta.fields + ['emergency_numbers', 'referrer', 'relatives', 'underlying_conditions']

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ['disease_id', 'name']

class VisitScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitSchedule
        fields = ['doctor_id', 'days_available', 'hours_per_day', 'average_visit_time', 'time_slot_interval']
