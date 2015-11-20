# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0050_auto_20151119_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductgroup',
            name='about',
            field=froala_editor.fields.FroalaField(verbose_name='Kursbeschreibung'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='conditions',
            field=froala_editor.fields.FroalaField(verbose_name='Zu den Angeboten'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='in_one_sentence',
            field=models.CharField(help_text='Beschreibe den Kurs in einem Satz', max_length=250, verbose_name='in einem Satz'),
        ),
        migrations.AlterField(
            model_name='courseproductgroup',
            name='mentors',
            field=froala_editor.fields.FroalaField(verbose_name='Kursleitung'),
        ),
    ]
