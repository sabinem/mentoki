# -*- coding: utf-8 -*-0023_auto_20150617_1038.py


"""
shell script:
from apps_data.courseevent.models.forum import Thread, Forum
from apps.forum.models import Thread as OldThread

threads = OldThread.objects.all()

for t in threads:
       forum = Forum.objects.get(oldsubforum=t.subforum)
       thread = Thread(title=t.title, text=t.text, author=t.author, forum=forum,
          courseevent= forum.courseevent, created=t.created, modified=t.modified,
          oldthread=t)
       thread.save()

from apps_data.courseevent.models.forum import Post
from apps.forum.models import Post as OldPost

posts = OldPost.objects.all()

for p in posts:
   thread = Thread.objects.get(oldthread=p.thread)
   post = Post(thread=thread, title=thread.title, text=p.text, author=p.author, courseevent=thread.forum.courseevent,
      created=p.created, modified=p.modified, oldpost=p)
   post.save()

"""


from __future__ import unicode_literals

from django.db import models, migrations

def transfer_subforums(apps, schema_editor):
    OldThread = apps.get_model("forum", "Thread")
    Thread = apps.get_model("courseevent", "Thread")
    NewForum = apps.get_model("courseevent", "Forum")

    threads = OldThread.objects.all().select_related('subforum')

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
        ('courseevent', '0025_datamigration_subforums'),
    ]

    operations = [
        migrations.RunPython(transfer_subforums)
    ]
