# Generated by Django 4.2 on 2023-04-16 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organdonation', '0006_alter_donor_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='email',
            field=models.EmailField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='recipient',
            name='email',
            field=models.EmailField(max_length=150, null=True),
        ),
    ]
