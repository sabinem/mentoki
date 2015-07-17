# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from data.courseevent.models import Forum
from apps.forum.models import SubForum

subforums = SubForum.objects.all().select_related('forum').filter(parentforum=None)

for s in subforums:
       parent = Forum.objects.get(oldforum=s.forum, parent=None)
       forum = Forum(title=s.title, text=s.text, oldsubforum=s, oldforum=s.forum,
          courseevent= s.forum.courseevent, created=s.created, modified=s.modified,
          can_have_threads=True, display_nr=s.display_nr)
       forum.insert_at(parent)
       forum.save()

Forum.objects.rebuild()

# repeat two times

subforums = SubForum.objects.all().select_related('forum').exclude(parentforum=None).order_by('parentforum_id')

for s in subforums:
    try:
       parent = Forum.objects.get(oldsubforum=s.parentforum)
       try:
           forum = Forum.objects.get(oldsubforum=s)
       except:
           forum = Forum(title=s.title, text=s.text, oldsubforum=s, oldforum=s.forum,
              courseevent= s.forum.courseevent, created=s.created, modified=s.modified,
              can_have_threads=True, display_nr=s.display_nr)
           forum.insert_at(parent)
           forum.save()
    except:
       pass


Forum.objects.rebuild()
"""


from __future__ import unicode_literals

from django.db import models, migrations

def transfer_subforums(apps, schema_editor):
    SubForum = apps.get_model("forum", "SubForum")
    NewForum = apps.get_model("courseevent", "Forum")

    subforums = SubForum.objects.all().select_related('forum').filter(parentforum=None)

    for subforum in subforums:

        parent = NewForum.objects.get(oldforum=subforum.forum, parent=None)

        forum = NewForum(title=subforum.title,
                         text=subforum.text,
                         courseevent=subforum.forum.courseevent,
                         oldsubforum=subforum,
                         created=subforum.created,
                         modified=subforum.modified,
                         oldforum=subforum.forum,
                         oldsubforum=subforum,
                         can_have_threads=False,
                         display_nr=subforum.display_nr)

        forum.insert_at(parent)
        forum.save()

    NewForum.objects.rebuild()

    subforums = SubForum.objects.all().select_related('forum').exclude(parentforum=None).order_by('level')

    for subforum in subforums:

        parent = NewForum.objects.get(oldforum=subforum.forum, parent=subforum.parentforum)

        forum = NewForum(title=subforum.title,
                         text=subforum.text,
                         courseevent=subforum.forum.courseevent,
                         oldsubforum=subforum,
                         created=subforum.created,
                         modified=subforum.modified,
                         oldforum=subforum.forum,
                         oldsubforum=subforum,
                         can_have_threads=False,
                         display_nr=subforum.display_nr)

        forum.insert_at(parent)
        forum.save()

    NewForum.objects.rebuild()


class Migration(migrations.Migration):

    dependencies = [
        ('courseevent', '0024_datamigration_forums'),
    ]

    operations = [
        migrations.RunPython(transfer_subforums)
    ]
