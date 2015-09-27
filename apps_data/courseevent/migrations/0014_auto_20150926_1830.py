# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0013_auto_20150924_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='is_archived',
            field=models.BooleanField(default=False, help_text='Archivierte Ver\xf6ffentlichungen sind im Klassenzimmer\n                    nicht mehr zu sehen.', verbose_name='archivieren'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='mail_distributor',
            field=models.TextField(help_text='email-Adressen, an die die Ank\xfcndigung geschickt wurde', null=True, verbose_name='Mail-Verteiler', blank=True),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='published',
            field=models.BooleanField(default=False, help_text='Beim Ver\xf6ffentlichen wird die Ank\xfcndigung an\n                    alle Kursteilnehmer und Mentoren verschickt:', verbose_name='ver\xf6ffentlichen?'),
        ),
    ]
