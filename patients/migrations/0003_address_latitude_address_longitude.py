# Generated by Django 5.0.2 on 2024-03-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_additionalfieldconfiguration_additionalfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
