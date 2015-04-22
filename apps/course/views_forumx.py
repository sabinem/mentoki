from __future__ import unicode_literals
import logging
# import from django
from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
# from other apps
from apps.forum.views_forum import ForumMixin
from apps.classroom.mixins import ClassroomMixin
# import from this app
from apps.forum.cache import recalc_forum_structure, recalc_subforum_change
from apps.forum.models import SubForum, Thread
from .forms_forum import SubForumCreateForm
from apps.courseevent.models import CourseEvent
from apps.forum.models import Forum
from .mixins import CourseEventBuildMixin
from apps.forum.views_forum import subforums_output_list

logger = logging.getLogger(__name__)


class ForumBuildView(ForumMixin, CourseEventBuildMixin, TemplateView):
    template_name = 'courseforum/forum.html'

    def get_context_data(self, **kwargs):
        context = super(ForumBuildView, self).get_context_data(**kwargs)
        logger.debug("---------- in ForumListView get_context_data")
        context['output_list'] = subforums_output_list(context, None)
        print context['courseevent']
        return context


class SubForumUpdateView(ForumMixin, CourseEventBuildMixin, UpdateView):

    template_name = 'courseforum/subforumupdate.html'
    context_object_name = 'subforum'

    def get_object(self, queryset=None):
        subforum = SubForum.objects.get(id=self.kwargs['subforum'])
        return subforum

    def get_form_class(self):
        threads = Thread.objects.filter(subforum_id=1)
        if threads.exists():
            self.form_class = SubForumReducedUpdateForm
        else:
            self.form_class = SubForumCompleteUpdateForm
        return self.form_class

    def get_success_url(self):
        self.messages.success("Das Unterforum wurde gespeichert.")
        recalc_forum_structure(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        return reverse('buildclassroom:buildforum', kwargs={"slug": self.kwargs['slug']})

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        if form.cleaned_data['display_number']:
            number = form.cleaned_data["display_number"]
            parentforum = form.cleaned_data["parentforum"]
            brotherforums = SubForum.objects.filter(parentforum=parentforum).exclude(id=form.instance.id).order_by('display_nr')
            count = 0
            for subforum in brotherforums:
                count += 1
                if count < number:
                    subforum.display_nr =  count
                elif count >= number:
                    subforum.display_nr =  count + 1
                subforum.save()
            form.instance.display_nr = number
        return super(SubForumUpdateView, self).form_valid(form)

    def get_form_kwargs(self):
        slug = self.kwargs['slug']
        courseevent = CourseEvent.objects.get(slug=slug)
        forum = Forum.objects.get(courseevent_id = courseevent.id)
        forum_id = forum.id
        kwargs = super(SubForumUpdateView, self).get_form_kwargs()
        kwargs['forum_id'] = forum_id
        return kwargs


class SubForumDeleteView(ForumMixin, CourseEventBuildMixin, DeleteView):

    template_name = 'courseforum/subforumdelete.html'
    model = SubForum

    def get_object(self, queryset=None):
        subforum = SubForum.objects.get(id=self.kwargs['subforum'])
        return subforum

    def get_success_url(self):
        self.messages.success("Das Unterforum wurde geloescht.")
        recalc_forum_structure(self.object.forum_id)
        recalc_subforum_change(self.object.forum_id)
        return reverse('buildclassroom:buildforum', kwargs={"slug": self.kwargs['slug']})



class SubForumCreateView(ForumMixin, CourseEventBuildMixin, CreateView):

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


