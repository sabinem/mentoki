# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0009_auto_20150826_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_forumlink',
            field=models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Forum'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_homeworklink',
            field=models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Aufgabe'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_lessonlink',
            field=models.BooleanField(default=False, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Lektion'),
        ),
        migrations.AddField(
            model_name='classroommenuitem',
            name='is_listlink',
            field=models.BooleanField(default=True, help_text='Links deren setzen Objekte im Klassenzimmer ver\xf6ffentlicht.\n        Das ist bei Lektionen und Foren der Fall', verbose_name='Liste'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='classlesson',
            field=models.OneToOneField(verbose_name='Bezug auf einen Lernabschnitt?', to='lesson.ClassLesson'),
        ),
    ]
