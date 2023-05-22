# Generated by Django 4.2 on 2023-05-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organdonation', '0018_rename_request_donor_is_accepted_donor_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='is_available',
        ),
        migrations.AddField(
            model_name='donor',
            name='is_pending',
            field=models.BooleanField(default=False),
        ),
    ]
