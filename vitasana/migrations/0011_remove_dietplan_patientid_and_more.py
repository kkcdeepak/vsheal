# Generated by Django 5.0 on 2023-12-23 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0010_avpariksha_basicinfoop_dietplan_nutritionaladvtb_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dietplan',
            name='patientid',
        ),
        migrations.RemoveField(
            model_name='nutritionaladvtb',
            name='dietplan_id',
        ),
        migrations.RemoveField(
            model_name='nutritionaladvtb',
            name='patientid',
        ),
        migrations.RemoveField(
            model_name='pathology',
            name='patientid',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='patientid',
        ),
        migrations.RemoveField(
            model_name='prescriptiondose',
            name='prescription_id',
        ),
        migrations.RemoveField(
            model_name='prescriptiondose',
            name='patientid',
        ),
        migrations.RemoveField(
            model_name='vitalstb',
            name='patientid',
        ),
        migrations.DeleteModel(
            name='AvPariksha',
        ),
        migrations.DeleteModel(
            name='DietPlan',
        ),
        migrations.DeleteModel(
            name='NutritionalAdvTb',
        ),
        migrations.DeleteModel(
            name='Pathology',
        ),
        migrations.DeleteModel(
            name='Prescription',
        ),
        migrations.DeleteModel(
            name='PrescriptionDose',
        ),
        migrations.DeleteModel(
            name='VitalsTb',
        ),
    ]
