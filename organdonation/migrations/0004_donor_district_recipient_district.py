# Generated by Django 4.2 on 2023-04-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organdonation', '0003_remove_donor_password2_remove_recipient_password2'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='district',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='recipient',
            name='district',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
