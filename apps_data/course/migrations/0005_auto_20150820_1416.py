# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20150819_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.EmailField(default='info@mentoki.com', help_text='Die email-Adresse des Kursleiters oder eine Mentoki-Adresse. Bitte\n        stimme diese Adresse mit Mentoki ab.', max_length=254, verbose_name='email Addresse f\xfcr den Kurs'),
        ),
        migrations.AlterField(
            model_name='course',
            name='project',
            field=models.TextField(help_text='Was nehmen Teilnehmer aus Deinem Kurs f\xfcr sich mit?', verbose_name='Teilnehmerprojekt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='structure',
            field=models.TextField(help_text='Gib eine Gliederung Deines Kurses an', verbose_name='Gliederung', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='text',
            field=models.TextField(help_text='Hier kannst Du Deinen Kurs ausf\xfchrlich beschreiben.', verbose_name='Kursbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
    ]
