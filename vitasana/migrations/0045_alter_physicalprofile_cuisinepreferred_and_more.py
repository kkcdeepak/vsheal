# Generated by Django 5.0 on 2024-01-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0044_alter_physicalprofile_cuisinepreferred_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalprofile',
            name='CuisinePreferred',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='physicalprofile',
            name='Description1',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='physicalprofile',
            name='Description2',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
