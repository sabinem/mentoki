# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.course
import apps_data.course.models.oldcoursepart


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0094_auto_20150811_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display_nr',
            field=models.IntegerField(default=1, help_text='Dieses Feld steuert die Anzeigereihenfolge bei mehreren Kursleitern.', verbose_name='Anzeigereihenfolge'),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen, das auf der Kursauschreibung\n        erscheinen soll.', upload_to=apps_data.course.models.course.foto_location, verbose_name='Kursleiter-Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(help_text='Personenbeschreibung: was qualifiziert Dich f\xfcr das Halten dieses\n        Kurses?', verbose_name='Kursleiterbeschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.CharField(help_text='diese Beschreibung erscheint nur in den \xdcbersichten', max_length=200, verbose_name='kurze Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_nr',
            field=models.CharField(help_text='abgeleitetes Feld: keine manuelle Eingabe', max_length=10, verbose_name='Lektionsnr.', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='materials',
            field=models.ManyToManyField(help_text='Material der Lektion', to='course.Material', verbose_name='Kursmaterial', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='nr',
            field=models.IntegerField(default=1, verbose_name='Nr.'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='text',
            field=models.TextField(help_text='Text der Lektion', verbose_name='Lektionstext', blank=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(help_text='Lektions-Titel', max_length=100, verbose_name='\xdcberschrift'),
        ),
    ]
