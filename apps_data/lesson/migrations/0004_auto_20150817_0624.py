# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0125_auto_20150817_0624'),
        ('lesson', '0003_auto_20150816_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='old_pk',
        ),
        migrations.AddField(
            model_name='lesson',
            name='courseblock',
            field=models.ForeignKey(related_name='lessonblock', blank=True, to='course.CourseBlock', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unit',
            field=models.ForeignKey(related_name='lessonunit', blank=True, to='course.CourseUnit', null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unitmaterial',
            field=models.ForeignKey(related_name='lessonmaterial', blank=True, to='course.CourseMaterialUnit', null=True),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='lesson_nr',
            field=models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', verbose_name='Lektionsnr.', max_length=10, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_nr',
            field=models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', verbose_name='Lektionsnr.', max_length=10, editable=False, blank=True),
        ),
    ]
