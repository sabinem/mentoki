# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0019_courseevent_autoslug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseevent',
            name='accepted_at',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='autoslug',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='booking_closed_at',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='price',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='pricemodel',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='courseevent',
            name='review_ready_at',
        ),
    ]
