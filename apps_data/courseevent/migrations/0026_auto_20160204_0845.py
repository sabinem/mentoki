# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0025_studentswork_feedback_spice'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseeventparticipation',
            name='notification_forum',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='courseeventparticipation',
            name='notification_work',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='classroommenuitem',
            name='item_type',
            field=models.CharField(help_text='Welcher Art ist der Men\xfceintrag: \xdcberschrift, Link, etc?', max_length=15, verbose_name='Typ des Men\xfcpunkts', choices=[('header', '\xdcberschrift'), ('lesson', 'Lektion'), ('forum', 'Forum'), ('announcements', 'Ank\xfcndigungsliste'), ('participants', 'Teilnehmerliste')]),
        ),
    ]
