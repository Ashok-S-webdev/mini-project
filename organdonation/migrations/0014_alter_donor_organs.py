# Generated by Django 4.2 on 2023-04-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organdonation', '0013_rename_organs_organ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='organs',
            field=models.ManyToManyField(related_name='donor', to='organdonation.organ'),
        ),
    ]
