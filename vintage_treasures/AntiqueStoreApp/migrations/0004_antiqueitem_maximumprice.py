# Generated by Django 3.0 on 2023-08-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AntiqueStoreApp', '0003_auto_20230823_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='antiqueitem',
            name='maximumprice',
            field=models.PositiveIntegerField(default=600),
        ),
    ]
