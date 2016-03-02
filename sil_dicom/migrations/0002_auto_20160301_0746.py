# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sil_dicom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image_size',
            field=models.CharField(max_length=255, editable=False),
        ),
    ]
