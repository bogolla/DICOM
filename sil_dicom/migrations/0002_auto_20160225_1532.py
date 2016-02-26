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
            name='size',
            field=models.IntegerField(null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='upload_date',
            field=models.DateTimeField(editable=False),
        ),
    ]
