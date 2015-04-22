import logging
from django.views.generic import TemplateView
from .mixins import ClassroomMixin
from .models import Announcement


logger = logging.getLogger(__name__)


class AnnouncementsListView(ClassroomMixin, TemplateView):
    template_name = 'classroom_announcements/announcementslist.html'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementsListView, self).get_context_data(**kwargs)
        logger.debug("---------- in AnnouncementsListView get_context_data")
        announcement_list = Announcement.objects.filter(courseevent = context['courseevent']['courseevent_id'],
            published=True).order_by('-published_at_date')
        context['announcement_list'] = announcement_list
        return context


class AnnouncementDetailView(ClassroomMixin, TemplateView):
    template_name = 'classroom_announcements/announcementdetail.html'
    model = Announcement
    context_object_name = 'announcement'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementDetailView, self).get_context_data(**kwargs)
        logger.debug("---------- in AnnouncementDetailView get_context_data")
        try:
            announcement = Announcement.objects.get(id = kwargs['id'])
            context['announcement'] = announcement
        except:
            pass
        return context