# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150327_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default=b'0', max_length=2, choices=[(b'0', b'noch unveroeffentlicht'), (b'1', b'Vorankuendigung'), (b'2', b'zur Buchung geoeffnet'), (b'3', b'Buchung abgeschlossen'), (b'4', b'Kursereignis abgeschlossen')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default=b'1', max_length=2, choices=[(b'1', b'im Aufbau'), (b'0', b'zur internen Buchung geoeffnet'), (b'2', b'keine interne Buchung mehr moeglich')]),
            preserve_default=True,
        ),
    ]
