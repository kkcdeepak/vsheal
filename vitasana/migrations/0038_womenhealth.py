# Generated by Django 5.0 on 2023-12-30 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0037_alter_avpariksha_av_pariksha_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenHealth',
            fields=[
                ('womenhealth_id', models.AutoField(primary_key=True, serialize=False)),
                ('menstrual_history', models.CharField(choices=[('Regular', 'Regular Cycle'), ('Irregular', 'Irregular Cycle')], max_length=20)),
                ('length_of_cycle', models.IntegerField(default=0)),
                ('duration_of_bleeding', models.IntegerField(default=0)),
                ('abnormal_record', models.CharField(max_length=100)),
                ('white_discharge', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('cramps_during_menstruation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('bloating_during_menstruation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('loose_stools_during_menstruation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('constipation_during_menstruation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('other_symptoms', models.TextField(blank=True)),
                ('number_of_pregnancies', models.PositiveIntegerField(default=0)),
                ('childbirth_type', models.CharField(max_length=50)),
                ('number_of_deliveries', models.PositiveIntegerField(default=0)),
                ('nature_of_deliveries', models.CharField(max_length=50)),
                ('complications_during_pregnancy', models.TextField(blank=True)),
                ('baby_birth_defects_or_complications', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitasana.basicinfo')),
            ],
        ),
    ]