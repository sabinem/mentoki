# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20151020_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='is_paid',
            new_name='is_valid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='definitive',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='attempted', max_length=12, choices=[('fix', 'Nicht mehr erstattbar'), ('paid', 'bezahlt'), ('attempted', 'versucht')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='Teilnehmer als Benutzer'),
        ),
    ]
