# Generated by Django 5.0 on 2023-12-26 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0025_habitsinfo_drinksperday_habitsinfo_yearsofdrinking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitsinfo',
            name='DrinksPerDay',
        ),
        migrations.RemoveField(
            model_name='habitsinfo',
            name='YearsOfDrinking',
        ),
    ]
