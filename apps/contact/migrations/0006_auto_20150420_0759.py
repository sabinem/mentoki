# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20150420_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='motivation',
            field=models.TextField(verbose_name='Warum brennst Du f\xfcr dieses Thema?', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='priorexperience',
            field=models.TextField(verbose_name='Hast Du schon Unterrichtserfahrungen online oder im Pr\xe4senzunterricht?', blank=True),
            preserve_default=True,
        ),
    ]
