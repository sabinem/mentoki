# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps_data.course.models.course
import apps_data.course.models.oldcoursepart
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0082_auto_20150805_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='excerpt',
            field=models.TextField(help_text='Diese Kurzbeschreibung dient sp\xe4ter als Vorlage\n                               bei der Ausschreibung Deiner Kurse', verbose_name='Kurze Zusammenfassung / Abstrakt', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.TextField(help_text='Welches Vorwissen wird in Deinem\n                               Kurses Voraussetzung?', verbose_name='Voraussetzungen', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='target_group',
            field=models.TextField(help_text='Die Zielgruppe f\xfcr Deinen Kurs.', verbose_name='Zielgruppe', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(help_text='Arbeitstitel f\xfcr Deinen Kurs. Er ist nicht \xf6ffentlich sichtbar.', max_length=100, verbose_name='Kurstitel'),
        ),
        migrations.AlterField(
            model_name='coursematerialunit',
            name='file',
            field=models.FileField(upload_to=apps_data.course.models.oldcoursepart.lesson_material_name, verbose_name='Datei', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display',
            field=models.BooleanField(default=True, help_text='Soll dieses Profil auf der Kursausschreibungsseite angezeigt werden?.', verbose_name='Anzeigen auf der Auschreibungsseite?'),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='display_nr',
            field=models.IntegerField(default=1, help_text='Dieses Feld steuert die Anzeigereihenfolge bei mehreren Kursleitern.', verbose_name='Anzeigereihenfolge bei mehreren Kursleitern'),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='foto',
            field=models.ImageField(help_text='Hier kannst Du ein Foto von Dir hochladen, das auf der Kursauschreibung\n                             erscheinen soll.', upload_to=apps_data.course.models.course.foto_location, verbose_name='Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='text',
            field=models.TextField(help_text='Personenbeschreibung: was qualifiziert Dich f\xfcr das Halten dieses\n                            Kurses?', verbose_name='Text', blank=True),
        ),
        migrations.AlterField(
            model_name='courseowner',
            name='user',
            field=models.ForeignKey(verbose_name='Kursleiter', to=settings.AUTH_USER_MODEL),
        ),
    ]
