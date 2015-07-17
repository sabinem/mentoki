# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0020_auto_20150616_1554'),
        ('courseevent', '0003_auto_20150614_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseeventLessonPublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published_at_date', models.DateTimeField(auto_now_add=True)),
                ('courseevent', models.ForeignKey(to='courseevent.CourseEvent')),
                ('lesson', models.ForeignKey(to='course.Lesson')),
            ],
        ),
    ]
