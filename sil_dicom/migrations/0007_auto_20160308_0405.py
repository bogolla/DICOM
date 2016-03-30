# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sil_dicom', '0006_document_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnifiedProcedureStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('patient_name', models.CharField(max_length=128)),
                ('accession_number', models.CharField(max_length=128)),
                ('requested_procedure_id', models.CharField(max_length=128)),
                ('requested_procedure_desc', models.TextField()),
                ('scheduled_station_AE_title', models.CharField(max_length=128)),
                ('scheduled_ups_desc', models.TextField()),
                ('ups_status', models.CharField(default='CREATED', max_length=128, choices=[('image/dcm', 'DCM'), ('image/png', 'PNG'), ('image/jpeg', 'JPEG')])),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='content_type',
            field=models.CharField(default='DCM', max_length=100, choices=[('image/dcm', 'DCM'), ('image/png', 'PNG'), ('image/jpeg', 'JPEG')]),
        ),
        migrations.AlterField(
            model_name='document',
            name='data',
            field=models.FileField(upload_to='documents'),
        ),
    ]
