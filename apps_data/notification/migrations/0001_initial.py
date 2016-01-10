# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0022_auto_20160107_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('notification_type', models.IntegerField(default=2)),
                ('description', models.TextField()),
                ('courseeventparticipation', models.ForeignKey(verbose_name='Kurs-Teilnahme', to='courseevent.CourseEventParticipation')),
                ('thread', models.ForeignKey(blank=True, to='courseevent.Thread', null=True)),
            ],
            options={
                'verbose_name': 'Benachrichtigung',
                'verbose_name_plural': 'Benachrichtigungen',
            },
        ),
    ]
