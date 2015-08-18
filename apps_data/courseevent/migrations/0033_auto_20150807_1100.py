# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0032_courseevent_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseevent',
            name='opened_at',
        ),
        migrations.AddField(
            model_name='courseevent',
            name='booking_closed_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking_closed']), monitor='status_external'),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='published_at',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, when=set(['booking']), monitor='status_external'),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='status_external',
            field=models.CharField(default='0', max_length=2, choices=[('0', 'not public'), ('1', 'open for booking'), ('1', 'booking closed'), ('2', 'open for preview')]),
        ),
        migrations.AlterField(
            model_name='courseevent',
            name='title',
            field=models.CharField(help_text='Kurstitel unter dem dieser Kurs ausgeschrieben wird.', max_length=100, verbose_name='Kurstitel'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='can_have_threads',
            field=models.BooleanField(default=True, help_text='Steuert, ob Beitr\xe4ge in diesem Unterforum gemacht werden k\xf6nnen,\n                  oder ob es nur zur Gliederung dient.', verbose_name='Beitr\xe4ge erlaubt'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='display_nr',
            field=models.IntegerField(help_text='Steuert die Anzeigereihenfolge der UnterForen innerhalb des \xfcbergeordneten Forums', verbose_name='Anzeigereihenfolge'),
        ),
        migrations.AlterField(
            model_name='forum',
            name='published',
            field=models.BooleanField(default=False, help_text='Zeigt an, ob das Forum im Klassenzimmer sichtbar ist.', verbose_name='ver\xf6ffentlicht'),
        ),
    ]
