from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    mobile_phone = models.CharField(max_length=15)
    home_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    national_code = models.CharField(max_length=10)
    birth_date = models.DateField()

    class Meta:
        abstract = True

class Admin(User):
    password = models.CharField(max_length=128)

class UserType(User):
    USER_TYPE_CHOICES = [
        ('doctor', 'Doctor'),
        ('assistant', 'Assistant'),
        ('patient', 'Patient'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

class Patient(User):
    emergency_numbers = models.JSONField(blank=True, null=True)
    referrer = models.CharField(max_length=100, blank=True, null=True)
    relatives = models.JSONField(blank=True, null=True)
    underlying_conditions = models.JSONField(blank=True, null=True)

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class VisitSchedule(models.Model):
    doctor_id = models.ForeignKey(UserType, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'})
    days_available = models.JSONField()  # List of days in a week
    hours_per_day = models.JSONField()   # List of time ranges for each day
    average_visit_time = models.IntegerField()  # in minutes
    time_slot_interval = models.IntegerField()  # in minutes
