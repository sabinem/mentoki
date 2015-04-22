# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0020_coursematerialunit_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('comment', models.TextField()),
                ('comment_status', models.CharField(default=b'g', max_length=2, choices=[(b'g', b'normal'), (b'1', b'wichtig')])),
                ('title', models.CharField(max_length=100)),
                ('course', models.ForeignKey(default=1, to='course.Course')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='coursecomments',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursecomments',
            name='user',
        ),
        migrations.DeleteModel(
            name='CourseComments',
        ),
    ]
