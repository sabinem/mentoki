# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0006_auto_20150622_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='published',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='published_at_date',
        ),
        migrations.AddField(
            model_name='announcement',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['published']), monitor='status'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='status',
            field=model_utils.fields.StatusField(default='draft', max_length=100, no_check_for_status=True, choices=[(0, 'dummy')]),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='accepted_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['accepted']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='format',
            field=models.TextField(verbose_name='Kursformat', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='opened_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='prerequisites',
            field=models.TextField(verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='project',
            field=models.TextField(verbose_name='Teilnehmernutzen', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['public']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='review_ready_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['review']), monitor='status_external'),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='structure',
            field=models.TextField(verbose_name='Gliederung', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='target_group',
            field=models.TextField(verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='text',
            field=models.TextField(verbose_name='freie Kursbeschreibung', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='video_url',
            field=models.CharField(max_length=100, verbose_name='K\xfcrzel des Videos bei You Tube ', blank=True),
        ),
        migrations.AddField(
            model_name='courseevent',
            name='workload',
            field=models.TextField(verbose_name='Arbeitsbelastung', blank=True),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='event_type',
            field=models.CharField(default='sl', max_length=2, choices=[('gg', 'gef\xfchrter Gruppenkurs'), ('sl', 'Selbstlernen')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'not public'), ('1', 'open for booking'), ('2', 'open for preview')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_internal',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'not public'), ('1', 'open for booking'), ('a', 'open for preview')]),
        ),
    ]
