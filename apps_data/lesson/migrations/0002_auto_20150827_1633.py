# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0002_remove_material_pdf_link'),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlesson',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='materials',
        ),
        migrations.AddField(
            model_name='classlesson',
            name='material',
            field=models.ForeignKey(blank=True, to='material.Material', help_text='Material der Lektion', null=True, verbose_name='Kursmaterial'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='material',
            field=models.ForeignKey(blank=True, to='material.Material', help_text='Material der Lektion', null=True, verbose_name='Kursmaterial'),
        ),
        migrations.AlterField(
            model_name='classlesson',
            name='original_lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='lesson.Lesson', null=True),
        ),
    ]
