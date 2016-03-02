# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sil_dicom', '0002_auto_20160301_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='study_description',
            field=models.CharField(max_length=255, editable=False),
            preserve_default=False,
        ),
    ]
