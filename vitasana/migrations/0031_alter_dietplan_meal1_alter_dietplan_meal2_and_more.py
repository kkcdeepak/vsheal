# Generated by Django 5.0 on 2023-12-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0030_rename_friday_meal1_dietplan_meal1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dietplan',
            name='MEAL1',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='MEAL2',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='MEAL3',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='MEAL4',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='MEAL5',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='dietplan',
            name='MEAL6',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
