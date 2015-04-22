from __future__ import unicode_literals
import logging
# import from django
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
# from other apps
from apps.forum.views_forum import ForumMixin
# import from this app
from apps.forum.cache import recalc_forum_structure, recalc_subforum_change
from apps.forum.models import SubForum, Thread
from .forms_forum import SubForumCreateForm
from apps.courseevent.models import CourseEvent
from apps.forum.models import Forum
from .mixins import CourseEventBuildMixin
from apps.forum.views_forum import subforums_output_list

logger = logging.getLogger(__name__)



class SubForumCreateView(CourseEventBuildMixin, CreateView):

    template_name = 'courseforum/subforumcreate.html'
    form_class = SubForumCreateForm

    def form_valid(self, form, **kwargs):
        print "----------- in valid 1"
        context = self.get_context_data(**kwargs)
        print "----------- in valid"
        form.instance.forum_id = context['courseevent']['forum_id']
        return super(SubForumCreateView, self).form_valid(form)

    def get_success_url(self):
        print "----------- in url"
        recalc_forum_structure(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        return reverse('course:buildforum', kwargs={"slug": self.kwargs['slug']})

    def get_form_kwargs(self):
        print "----------- in kwargs"
        slug = self.kwargs['slug']
        courseevent = CourseEvent.objects.get(slug=slug)
        forum = Forum.objects.get(courseevent_id = courseevent.id)
        forum_id = forum.id
        kwargs = super(SubForumCreateView, self).get_form_kwargs()
        kwargs['forum_id'] = forum_id
        return kwargs


