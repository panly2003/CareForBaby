# Generated by Django 3.2 on 2022-12-07 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='openid',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
