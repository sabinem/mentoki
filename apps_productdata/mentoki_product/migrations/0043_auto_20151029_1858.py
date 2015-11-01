# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0016_auto_20150929_1005'),
        ('mentoki_product', '0042_auto_20151029_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='courseevent',
            field=models.ForeignKey(blank=True, to='courseevent.CourseEvent', null=True),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='courseproduct',
            field=models.OneToOneField(null=True, blank=True, to='mentoki_product.CourseProduct'),
        ),
        migrations.AddField(
            model_name='specialoffer',
            name='reach',
            field=models.CharField(default=b'course', max_length=10, choices=[(b'course', 'course'), (b'courseevent', 'courseevent'), (b'product', 'product')]),
        ),
        migrations.AlterField(
            model_name='specialoffer',
            name='course',
            field=models.ForeignKey(blank=True, to='course.Course', null=True),
        ),
    ]
