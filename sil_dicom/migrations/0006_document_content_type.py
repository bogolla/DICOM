# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sil_dicom', '0005_auto_20160301_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='content_type',
            field=models.CharField(default=b'DCM', max_length=100, choices=[(b'image/png', b'PNG'), (b'image/jpeg', b'JPEG'), (b'image/dcm', b'DCM')]),
        ),
    ]
