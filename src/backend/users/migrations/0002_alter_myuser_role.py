# Generated by Django 3.2 on 2022-10-28 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('NURSE', 'Nurse'), ('ADMIN', 'Admin')], max_length=10),
        ),
    ]
