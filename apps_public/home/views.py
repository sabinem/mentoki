# -*- coding: utf-8 -*-

"""
Public pages that describe mentoki. Most of these pages are build dynamically
with text chunks that are fetched from the database.
"""

from __future__ import unicode_literals

from django.views.generic import TemplateView, DetailView
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from apps_accountdata.userprofiles.models.mentor import MentorsProfile
from apps_pagedata.textchunks.models import PublicTextChunks
from accounts.models import User
from apps_productdata.mentoki_product.models.courseproductgroup import CourseProductGroup
from apps_pagedata.public.models import StaticPublicPages

import logging
logger = logging.getLogger('public.dataintegrity')

class PageTextMixin(object):
    """
    Mixin for all pages that include text chunks from the table
    PublicTextChunks. The text is fetched with a pagecode that is in the
    page url.
    """
    context_object_name = 'textchunk'

    def get_object(self, queryset=None):
        """
        The text of the html page is fetched from the Table
        PublicTextChunks. If the text is not found a 404 page is displayed
        and the error is reported.
        """
        pagecode = self.kwargs['pagecode']
        try:
            textchunk = PublicTextChunks.objects.get(pagecode=pagecode)
            logger.info('textchunk found')
            return textchunk
        except ObjectDoesNotExist:
            logger.error('Text für die Seite [%s] nicht gefunden. Der '
                         'Seitencode mit dem gesucht wurde war: [%s]. '
                         'Gesucht wurde in der Tabelle [%s]'
                         % (self.template_name, pagecode,
                            PublicTextChunks.__name__))
            raise Http404
        except MultipleObjectsReturned:
            logger.error('Für die Seite [%s] wurden mehrere Texte gefunden. '
                         'Der Seitencode mit dem gesucht wurde war: [%s]. '
                         'Gesucht wurde in der Tabelle [%s]'
                         % (self.template_name, pagecode,
                            PublicTextChunks.__name__))
            raise Http404


class HomePageView(TemplateView):
    """
    Homepage
    """
    template_name = "home/pages/homepage.html"


class PublicPageView(
    DetailView):
    """
    public page
    """
    model = StaticPublicPages
    template_name = "home/pages/publicpage.html"
    context_object_name = 'pagedata'


class MentorsListView(TemplateView):
    """
    List of all of Mentokis mentors.
    """
    template_name = "home/pages/mentors.html"

    def get_context_data(self, **kwargs):
        context = super(MentorsListView, self).get_context_data()
        mentors = MentorsProfile.objects.all().select_related('user').order_by('display_nr')
        context['mentors'] = mentors
        return context


#TODO change this view and how it is called: it should be called with the slug!
class MentorsPageView(DetailView):
    """
    One mentor is displayed in detail along with his courses.
    """
    models = MentorsProfile
    context_object_name = 'mentor'
    template_name = "home/pages/mentor.html"

    def get_queryset(self):
        return MentorsProfile.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(MentorsPageView, self).get_context_data()
        mentor = context['mentor']
        context['courseproductgroups'] = \
            CourseProductGroup.objects.published_by_mentor(user=mentor.user)
        return context

