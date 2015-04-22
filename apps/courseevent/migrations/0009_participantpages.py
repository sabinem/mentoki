# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0008_courseeventparticipation_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantPages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('url', models.URLField(default=b'x', blank=True)),
                ('title', models.CharField(max_length=100)),
                ('participation', models.ForeignKey(to='courseevent.CourseEventParticipation')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
