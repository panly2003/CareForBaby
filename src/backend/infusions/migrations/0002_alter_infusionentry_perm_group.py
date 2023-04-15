# Generated by Django 3.2 on 2022-11-09 14:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('infusions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infusionentry',
            name='perm_group',
            field=models.ManyToManyField(blank=True, related_name='perm_group_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
