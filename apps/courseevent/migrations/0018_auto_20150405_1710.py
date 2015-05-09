# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0017_auto_20150403_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'noch unver\xf6ffentlicht'), ('1', 'Vorank\xfcndigung'), ('2', 'zur Buchung ge\xf6ffnet'), ('3', 'Buchung abgeschlossen'), ('4', 'Kursereignis abgeschlossen')]),
            preserve_default=True,
        ),
    ]
