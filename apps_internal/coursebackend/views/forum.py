# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

from vanilla import TemplateView, DetailView, UpdateView, FormView, DeleteView

from apps_data.courseevent.models.forum import Forum
from apps_data.courseevent.models.courseevent import CourseEvent

from ..forms.forum import ForumChangeForm
from .mixins.base import CourseMenuMixin


class ForumMixin(CourseMenuMixin):

    def get_success_url(self):
       """
       for create update and delete view
       """
       return reverse_lazy('classroom:studentswork:list',
                           kwargs={'slug': self.kwargs['slug']})


class ForumListView(ForumMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumListView, self).get_context_data(**kwargs)

        context['nodes'] = Forum.objects.forums_for_courseevent(courseevent=context['courseevent'])
        print context['nodes']

        return context


class ForumDetailView(CourseMenuMixin, TemplateView):
    """
    List all lesson blocks with lessons underneath
    """
    def get_context_data(self, **kwargs):
        context = super(ForumDetailView, self).get_context_data(**kwargs)

        forum = get_object_or_404(Forum, pk=self.kwargs['pk'])

        context['forum'] = forum
        context['breadcrumbs'] = forum.get_ancestors()
        context['nodes'] = forum.get_descendants()

        return context





class ForumDetailView(ForumMixin, DetailView):
    """
    Work Detail
    """
    template_name = 'classroom/studentswork/pages/detail.html'
    model = Forum
    lookup_field = 'pk'
    context_object_name ='work'


class ForumUpdateView(ForumMixin, UpdateView):
    """
    Work Update
    """
    template_name = 'classroom/studentswork/pages/update.html'
    model = Forum
    form_class = ForumChangeForm
    lookup_field = 'pk'
    context_object_name ='work'


class ForumDeleteView(ForumMixin, DeleteView):
    """
    Work Delete
    """
    template_name = 'classroom/studentswork/pages/delete.html'
    model = Forum
    lookup_field = 'pk'
    context_object_name ='work'


class ForumCreateView(ForumMixin, FormView):
    """
    Forum Create
    """
    model = Forum
    form_class = ForumChangeForm
    context_object_name ='forum'

    def get(self, request, *args, **kwargs):
        courseevent = get_object_or_404(CourseEvent,slug=self.kwargs['slug'])
        form = self.get_form()
        form.fields['parent'].queryset = \
            Forum.objects.parent_choice_for_forum(courseevent=courseevent)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    def form_valid(self, form):
        courseevent = get_object_or_404(CourseEvent, slug=self.kwargs['slug'])
        Forum.objects.create_new_work(
            courseevent=courseevent,
            homework=form.cleaned_data['homework'],
            text=form.cleaned_data['text'],
            title=form.cleaned_data['title'],
            user=self.request.user)

        return HttpResponseRedirect(self.get_success_url())

