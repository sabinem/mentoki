# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from vanilla import RedirectView

from apps_data.courseevent.models.menu import ClassroomMenuItem

from .mixins.base import ClassroomMenuMixin



class ClassroomStartView(ClassroomMenuMixin, RedirectView):
    permanent = False
    """
    Start in this section of the website: it shows the course and its attributes
    """
    def get_redirect_url(self, *args, **kwargs):

        startitem = ClassroomMenuItem.objects.get_startitem_from_slug(courseevent_slug=self.kwargs['slug'])

        if startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.announcements:
            url = reverse('classroom:announcement:list', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.forum_item:
            kwargs['pk'] = startitem.forum_id
            url = reverse('classroom:forum:detail', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.homework:
            kwargs['pk'] = startitem.forum_id
            url = reverse('classroom:homework:list', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.forum_last_posts:
            url = reverse('classroom:forum:newposts', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.student_private:
            url = reverse('classroom:studentswork:list', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.lesson_item:
            kwargs['pk'] = startitem.lesson_id
            url = reverse('classroom:lesson:detail', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.participants_list:
            url = reverse('classroom:participant:list', args=args, kwargs=kwargs)
            return url
