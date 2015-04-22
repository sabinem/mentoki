# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0047_auto_20150410_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseblock',
            name='show_full',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
