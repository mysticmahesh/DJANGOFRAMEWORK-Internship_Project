# Generated by Django 3.2.21 on 2023-09-21 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AntiqueStoreApp', '0010_auto_20230908_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]