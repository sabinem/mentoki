# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0014_courseeventparticipation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'noch unveroeffentlicht'), (b'2', b'zur Buchung geoeffnet'), (b'3', b'Buchung abgeschlossen'), (b'4', b'offen fuer interne Buchung')]),
            preserve_default=True,
        ),
    ]
