# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('data', models.FileField(upload_to=b'documents')),
                ('upload_date', models.DateTimeField(editable=False)),
                ('image_size', models.IntegerField(editable=False)),
                ('patient_name', models.CharField(max_length=255, editable=False)),
                ('patient_id', models.CharField(max_length=14, editable=False)),
                ('patient_age', models.CharField(max_length=14, editable=False)),
                ('body_part_examined', models.CharField(max_length=255, editable=False)),
                ('study_date', models.DateTimeField(editable=False)),
                ('study_uid', models.CharField(max_length=255, editable=False)),
                ('study_instance_uid', models.CharField(max_length=255, editable=False)),
                ('series_number', models.CharField(max_length=255, editable=False)),
                ('series_instance_uid', models.CharField(max_length=255, editable=False)),
            ],
        ),
    ]
