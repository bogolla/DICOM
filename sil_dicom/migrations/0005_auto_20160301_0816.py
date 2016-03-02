# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sil_dicom', '0004_auto_20160301_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='study_uid',
        ),
        migrations.AddField(
            model_name='document',
            name='study_id',
            field=models.CharField(max_length=255, editable=False),
            preserve_default=False,
        ),
    ]
