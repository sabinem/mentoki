# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentoki_product', '0058_courseproductgroup_menu_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseproductgroup',
            name='in_one_sentence',
            field=froala_editor.fields.FroalaField(help_text='Beschreibe den Kurs in einem Satz', verbose_name='in einem Satz'),
        ),
    ]
