# Generated by Django 5.0 on 2023-12-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0018_alter_physicalprofile_foodpreferences'),
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
        migrations.AlterField(
            model_name='physicalprofile',
            name='DigestiveIssues',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
