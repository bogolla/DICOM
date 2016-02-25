# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.FileField(upload_to=b'documents')),
                ('title', models.CharField(max_length=255)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('size', models.IntegerField(help_text=b'The size of the attachment in bytes')),
            ],
        ),
    ]
