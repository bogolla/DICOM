# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sil_dicom', '0003_document_study_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='study_uid',
            field=models.CharField(unique=True, max_length=255, editable=False),
        ),
    ]
