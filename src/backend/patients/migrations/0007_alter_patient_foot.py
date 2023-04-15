# Generated by Django 3.2 on 2022-12-09 19:31

from django.db import migrations, models
import patients.models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_alter_patient_foot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='foot',
            field=models.ImageField(blank=True, null=True, upload_to=patients.models.upload_to, verbose_name='Image'),
        ),
    ]
