# Generated by Django 5.1 on 2024-08-31 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile_phone', models.CharField(max_length=15)),
                ('home_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('national_code', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile_phone', models.CharField(max_length=15)),
                ('home_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('national_code', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('emergency_numbers', models.JSONField(blank=True, null=True)),
                ('referrer', models.CharField(blank=True, max_length=100, null=True)),
                ('relatives', models.JSONField(blank=True, null=True)),
                ('underlying_conditions', models.JSONField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('mobile_phone', models.CharField(max_length=15)),
                ('home_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('national_code', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('user_type', models.CharField(choices=[('doctor', 'Doctor'), ('assistant', 'Assistant'), ('patient', 'Patient')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VisitSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_available', models.JSONField()),
                ('hours_per_day', models.JSONField()),
                ('average_visit_time', models.IntegerField()),
                ('time_slot_interval', models.IntegerField()),
                ('doctor_id', models.ForeignKey(limit_choices_to={'user_type': 'doctor'}, on_delete=django.db.models.deletion.CASCADE, to='myapp.usertype')),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
