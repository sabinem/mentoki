# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_contact_prebooking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prebooking',
            options={'verbose_name': 'Voranmeldung', 'verbose_name_plural': 'Voranmeldung'},
        ),
        migrations.RemoveField(
            model_name='prebooking',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='prebooking',
            name='last_name',
        ),
        migrations.AddField(
            model_name='prebooking',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Name', blank=True),
        ),
        migrations.AlterField(
            model_name='prebooking',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='prebooking',
            name='interested_in_learning',
            field=models.ForeignKey(verbose_name='Kurs', to='mentoki_product.CourseProductGroup'),
        ),
        migrations.AlterField(
            model_name='prebooking',
            name='message',
            field=models.TextField(verbose_name='Ihre Nachricht'),
        ),
    ]
