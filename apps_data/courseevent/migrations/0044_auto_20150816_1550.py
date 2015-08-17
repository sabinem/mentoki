# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0043_auto_20150814_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseeventlessonpublish',
            name='courseevent',
        ),
        migrations.RemoveField(
            model_name='courseeventlessonpublish',
            name='lesson',
        ),
        migrations.DeleteModel(
            name='ForumMenuItem',
        ),
        migrations.DeleteModel(
            name='CourseeventLessonPublish',
        ),
    ]
