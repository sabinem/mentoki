# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0009_simpleproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseeventproduct',
            old_name='brutto',
            new_name='mwst',
        ),
        migrations.RenameField(
            model_name='courseeventproduct',
            old_name='provision',
            new_name='netto_vk',
        ),
        migrations.RenameField(
            model_name='courseeventproduct',
            old_name='tax',
            new_name='provision_mentoki',
        ),
        migrations.RenameField(
            model_name='simpleproduct',
            old_name='brutto',
            new_name='mwst',
        ),
        migrations.RenameField(
            model_name='simpleproduct',
            old_name='tax',
            new_name='netto_vk',
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='currency',
            field=models.CharField(default='EUR', max_length=3, choices=[('EUR', 'Euro'), ('CHF', 'Schweizer Franken')]),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='event_type',
            field=models.CharField(default='selflearn', max_length=12, verbose_name='Kursart', choices=[('guided', 'gef\xfchrter Gruppenkurs'), ('selflearn', 'Selbstlernen'), ('coached', 'Selbstlernen mit Unterst\xfctzung')]),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='mentoki_mwst',
            field=models.DecimalField(null=True, verbose_name='Mentoki Mehrwertsteuer', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='courseeventproduct',
            name='mentoki_netto',
            field=models.DecimalField(null=True, verbose_name='Mentoki Provision netto', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='currency',
            field=models.CharField(default='EUR', max_length=3, choices=[('EUR', 'Euro'), ('CHF', 'Schweizer Franken')]),
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='event_type',
            field=models.CharField(default='selflearn', max_length=12, verbose_name='Kursart', choices=[('guided', 'gef\xfchrter Gruppenkurs'), ('selflearn', 'Selbstlernen'), ('coached', 'Selbstlernen mit Unterst\xfctzung')]),
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='mentoki_mwst',
            field=models.DecimalField(null=True, verbose_name='Mentoki Mehrwertsteuer', max_digits=12, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='simpleproduct',
            name='mentoki_netto',
            field=models.DecimalField(null=True, verbose_name='Mentoki Provision netto', max_digits=12, decimal_places=2, blank=True),
        ),
    ]
