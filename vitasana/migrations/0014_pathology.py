# Generated by Django 5.0 on 2023-12-23 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0013_rename_vitalstb_vitals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pathology',
            fields=[
                ('pathology_id', models.IntegerField(primary_key=True, serialize=False)),
                ('BloodTestsAdvisedDate', models.DateField(null=True)),
                ('BloodReportsSummaryDate', models.DateField(null=True)),
                ('MentionBloodOutcome', models.CharField(choices=[('High', 'High'), ('Low', 'Low')], max_length=4, null=True)),
                ('ScanReportsAdvisedDate', models.DateField(null=True)),
                ('MentionScanOutcome', models.CharField(choices=[('Abnormality', 'Abnormality'), ('Risk', 'Risk')], max_length=11, null=True)),
                ('SummaryOfReports', models.CharField(max_length=500, null=True)),
                ('FinalDiagnosis', models.CharField(max_length=500, null=True)),
                ('MedicationDosage', models.CharField(max_length=100, null=True)),
                ('MedicationDurations', models.CharField(max_length=100, null=True)),
                ('DietDos', models.CharField(max_length=500, null=True)),
                ('DietDonts', models.CharField(max_length=500, null=True)),
                ('LifestyleDos', models.CharField(max_length=500, null=True)),
                ('LifestyleDonts', models.CharField(max_length=500, null=True)),
                ('DiseasePrognosis', models.CharField(choices=[('good', 'good'), ('manageable', 'manageable'), ('bad', 'bad'), ('incurable', 'incurable')], max_length=10, null=True)),
                ('FollowUpScheduleDate', models.DateField(null=True)),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitasana.basicinfo')),
            ],
        ),
    ]
