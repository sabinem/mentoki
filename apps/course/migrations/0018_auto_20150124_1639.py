# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_coursematerialunit_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='document',
            field=models.ForeignKey(to='pdf.Document'),
            preserve_default=True,
        ),
    ]
