# Generated by Django 5.0 on 2023-12-23 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0016_prescription_prescriptiondose'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('dietplan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('DietryGuidance', models.TextField(null=True)),
                ('RECIPES', models.TextField(null=True)),
                ('ANALYSISOFDIET', models.TextField(null=True)),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitasana.basicinfo')),
            ],
        ),
        migrations.CreateModel(
            name='NutritionalAdv',
            fields=[
                ('nutritionaladv_id', models.AutoField(primary_key=True, serialize=False)),
                ('MONDAY_MEAL0', models.TextField(null=True)),
                ('MONDAY_MEAL1', models.TextField(null=True)),
                ('MONDAY_MEAL2', models.TextField(null=True)),
                ('TUESDAY_MEAL0', models.TextField(null=True)),
                ('TUESDAY_MEAL1', models.TextField(null=True)),
                ('TUESDAY_MEAL2', models.TextField(null=True)),
                ('WEDNESDAY_MEAL0', models.TextField(null=True)),
                ('WEDNESDAY_MEAL1', models.TextField(null=True)),
                ('WEDNESDAY_MEAL2', models.TextField(null=True)),
                ('THURSDAY_MEAL0', models.TextField(null=True)),
                ('THURSDAY_MEAL1', models.TextField(null=True)),
                ('THURSDAY_MEAL2', models.TextField(null=True)),
                ('FRIDAY_MEAL0', models.TextField(null=True)),
                ('FRIDAY_MEAL1', models.TextField(null=True)),
                ('FRIDAY_MEAL2', models.TextField(null=True)),
                ('SATURDAY_MEAL0', models.TextField(null=True)),
                ('SATURDAY_MEAL1', models.TextField(null=True)),
                ('SATURDAY_MEAL2', models.TextField(null=True)),
                ('SUNDAY_MEAL0', models.TextField(null=True)),
                ('SUNDAY_MEAL1', models.TextField(null=True)),
                ('SUNDAY_MEAL2', models.TextField(null=True)),
                ('dietplan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitasana.dietplan')),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitasana.basicinfo')),
            ],
        ),
    ]
