# Generated by Django 5.0 on 2023-12-26 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0029_dietplan_dietician_dietplan_friday_meal1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dietplan',
            old_name='FRIDAY_MEAL1',
            new_name='MEAL1',
        ),
        migrations.RenameField(
            model_name='dietplan',
            old_name='FRIDAY_MEAL2',
            new_name='MEAL2',
        ),
        migrations.RenameField(
            model_name='dietplan',
            old_name='FRIDAY_MEAL3',
            new_name='MEAL3',
        ),
        migrations.RenameField(
            model_name='dietplan',
            old_name='FRIDAY_MEAL4',
            new_name='MEAL4',
        ),
        migrations.RenameField(
            model_name='dietplan',
            old_name='FRIDAY_MEAL5',
            new_name='MEAL5',
        ),
        migrations.RenameField(
            model_name='dietplan',
            old_name='FRIDAY_MEAL6',
            new_name='MEAL6',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='MONDAY_MEAL1',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='MONDAY_MEAL2',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='MONDAY_MEAL3',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='MONDAY_MEAL4',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='MONDAY_MEAL5',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='MONDAY_MEAL6',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SATURDAY_MEAL1',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SATURDAY_MEAL2',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SATURDAY_MEAL3',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SATURDAY_MEAL4',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SATURDAY_MEAL5',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SATURDAY_MEAL6',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SUNDAY_MEAL1',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SUNDAY_MEAL2',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SUNDAY_MEAL3',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SUNDAY_MEAL4',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SUNDAY_MEAL5',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='SUNDAY_MEAL6',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='THURSDAY_MEAL1',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='THURSDAY_MEAL2',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='THURSDAY_MEAL3',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='THURSDAY_MEAL4',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='THURSDAY_MEAL5',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='THURSDAY_MEAL6',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='TUESDAY_MEAL1',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='TUESDAY_MEAL2',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='TUESDAY_MEAL3',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='TUESDAY_MEAL4',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='TUESDAY_MEAL5',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='TUESDAY_MEAL6',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='WEDNESDAY_MEAL1',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='WEDNESDAY_MEAL2',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='WEDNESDAY_MEAL3',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='WEDNESDAY_MEAL4',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='WEDNESDAY_MEAL5',
        ),
        migrations.RemoveField(
            model_name='dietplan',
            name='WEDNESDAY_MEAL6',
        ),
    ]
