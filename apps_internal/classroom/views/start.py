# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.generic import RedirectView

from apps_data.courseevent.models.menu import ClassroomMenuItem

from .mixins.base import ClassroomMenuMixin


class ClassroomStartView(
    ClassroomMenuMixin,
    RedirectView):
    """
    redirects to the start-item in the menu when entering the classroom
    """
    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        try:
            startitem = ClassroomMenuItem.objects.get_startitem_from_slug(slug=self.kwargs['slug'])
        except ObjectDoesNotExist:
            return reverse('classroom:announcement:list', args=args, kwargs=kwargs)

        if startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.announcements_item:
            url = reverse('classroom:announcement:list', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.forum_item:
            kwargs['pk'] = startitem.forum_id
            url = reverse('classroom:forum:detail', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.homework_item:
            kwargs['pk'] = startitem.forum_id
            url = reverse('classroom:homework:list', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.last_posts_item:
            url = reverse('classroom:forum:newposts', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.private_item:
            url = reverse('classroom:studentswork:list', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.lesson_item:
            kwargs['pk'] = startitem.classlesson_id
            url = reverse('classroom:lesson:lesson_detail', args=args, kwargs=kwargs)
            return url

        elif startitem.item_type == ClassroomMenuItem.MENU_ITEM_TYPE.participants_item:
            url = reverse('classroom:participant:list', args=args, kwargs=kwargs)
            return url