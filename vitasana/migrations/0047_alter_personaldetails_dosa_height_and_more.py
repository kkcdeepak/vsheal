# Generated by Django 5.0 on 2024-01-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitasana', '0046_alter_physicalprofile_cuisinepreferred_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personaldetails_dosa',
            name='height',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='personaldetails_dosa',
            name='weight',
            field=models.DecimalField(decimal_places=6, max_digits=10, null=True),
        ),
    ]
