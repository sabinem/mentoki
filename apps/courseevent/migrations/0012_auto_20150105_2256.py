# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0011_remove_courseeventparticipation_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantpage',
            name='participation',
        ),
        migrations.AddField(
            model_name='participantpage',
            name='courseevent',
            field=models.ForeignKey(default=1, to='courseevent.CourseEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participantpage',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
