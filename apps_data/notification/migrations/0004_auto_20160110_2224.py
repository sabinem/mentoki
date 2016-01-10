# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courseevent', '0022_auto_20160107_2055'),
        ('notification', '0003_remove_classroomnotification_courseeventparticipation'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroomnotification',
            name='courseevent',
            field=models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True),
        ),
        migrations.AddField(
            model_name='classroomnotification',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
