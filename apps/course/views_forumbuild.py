# coding: utf-8
from __future__ import unicode_literals, absolute_import
# import from python
import logging
# import from django
from django.views.generic import CreateView, UpdateView, TemplateView
from django.core.urlresolvers import reverse
# import from own app
from .mixins import CourseEventBuildMixin
from apps.forum.cache import recalc_forum_structure, recalc_subforum_change
from .models import CourseUnit, CourseMaterialUnit, CourseBlock
from .forms_lessons import BlockForm, UnitForm, MaterialForm
from apps.forum.models import SubForum, Forum
from apps.courseevent.models import CourseEvent
from .forms_buildforum import SubForumForm
from apps.forum.views_forum import subforums_output_list
from apps.forum.views_forum import ForumMixin


logger = logging.getLogger(__name__)


class ForumBuildView(ForumMixin, CourseEventBuildMixin, TemplateView):
    template_name = 'courseforum/forum.html'

    def get_context_data(self, **kwargs):
        context = super(ForumBuildView, self).get_context_data(**kwargs)
        logger.debug("---------- in ForumListView get_context_data")
        context['output_list'] = subforums_output_list(context, None)
        print context['courseevent']
        return context


class SubForumCreateView(CourseEventBuildMixin, CreateView):
    model = SubForum
    form_class = SubForumForm
    template_name = 'forumbuild/subforumcreate.html'
    context_object_name = 'subforum'

    def get_form_kwargs(self):
        slug = self.kwargs['slug']
        courseevent = CourseEvent.objects.get(slug=slug)
        forum = Forum.objects.get(courseevent_id = courseevent.id)
        forum_id = forum.id
        kwargs = super(SubForumCreateView, self).get_form_kwargs()
        kwargs['forum_id'] = forum_id
        return kwargs

    def form_valid(self, form, **kwargs):
        courseevent = CourseEvent.objects.get(slug=self.kwargs['ce_slug'])
        forum = Forum.objects.get(courseevent_id = courseevent.id)
        form.instance.forum_id = forum.id
        return super(SubForumCreateView, self).form_valid(form)

    def get_success_url(self):
        print "----------- in url"
        recalc_forum_structure(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        return reverse('course:buildforum', kwargs={"slug": self.kwargs['slug'],
                                                    "ce_slug": self.kwargs['ce_slug']})


class SubForumUpdateView(CourseEventBuildMixin, UpdateView):
    model = SubForum
    form_class = SubForumForm
    template_name = 'forumbuild/subforumupdate.html'
    context_object_name = 'subforum'

    def get_form_kwargs(self):
        slug = self.kwargs['slug']
        courseevent = CourseEvent.objects.get(slug=slug)
        forum = Forum.objects.get(courseevent_id = courseevent.id)
        forum_id = forum.id
        kwargs = super(SubForumUpdateView, self).get_form_kwargs()
        kwargs['forum_id'] = forum_id
        return kwargs

    def get_success_url(self):
        print "----------- in url"
        recalc_forum_structure(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        return reverse('course:buildforum', kwargs={"slug": self.kwargs['slug'],
                                                    "ce_slug": self.kwargs['ce_slug']})
