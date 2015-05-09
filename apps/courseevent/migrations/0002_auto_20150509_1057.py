# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0001_squashed_0032_remove_courseeventpubicinformation_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseevent',
            name='course',
            field=models.ForeignKey(verbose_name='Kursvorlage', to='course.Course'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='excerpt',
            field=models.TextField(verbose_name='Abstrakt', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='max_participants',
            field=models.IntegerField(null=True, verbose_name='maximale Teilnehmeranzahl', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='nr_weeks',
            field=models.IntegerField(null=True, verbose_name='L\xe4nge in Wochen', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Startdatum', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseeventunitpublish',
            name='courseevent',
            field=models.ForeignKey(verbose_name='Kursereignis', to='courseevent.CourseEvent'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseeventunitpublish',
            name='published_at_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='ver\xf6ffentlicht am'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='courseeventunitpublish',
            name='unit',
            field=models.ForeignKey(verbose_name='Lektion', to='course.CourseUnit'),
            preserve_default=True,
        ),
    ]
