# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0124_auto_20150816_1653'),
        ('courseevent', '0044_auto_20150816_1550'),
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
            options={
                'verbose_name': 'XLessonPublish',
            },
        ),
    ]
