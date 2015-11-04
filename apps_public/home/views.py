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


class AGBPageView(
    PageTextMixin,
    DetailView):
    """
    The Offers and conditions of a course are described here.
    """
    template_name = "home/pages/agb.html"


class StandardPageView(
    PageTextMixin,
    DetailView):
    """
    Page that describes the mentoki standards
    """
    template_name = "home/pages/standards.html"


class TeachOnlinePageView(
    PageTextMixin,
    DetailView):
    """
    Page that describes how educators can start to teach online
    """
    template_name = "home/pages/unterrichten.html"


class CourseReadyPageView(
    PageTextMixin,
    DetailView):
    """
    Page for educators who already have a ready to go online course
    """
    template_name = "home/pages/fertigen-kurs-anbieten.html"


class EducationMentoringPageView(
    PageTextMixin,
    DetailView):
    """
    Page that describes mentokis offer of mentoring for education
    """
    template_name = "home/pages/bildungsmentoring.html"


class AboutPageView(TemplateView):
    """
    about page: about mentoki
    """
    template_name = "home/pages/about.html"


class ImpressumPageView(
    PageTextMixin,
    DetailView):
    """
    Impressum page
    """
    template_name = "home/pages/impressum.html"


class StarterkursPageView(
    PageTextMixin,
    DetailView):
    """
    page on mentokis starterkurs
    """
    template_name = "home/pages/starterkurs.html"


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


class MentorsPageView(TemplateView):
    """
    One mentor is displayed in detail along with his courses.
    """
    template_name = "home/pages/mentor.html"

    def get_context_data(self, **kwargs):
        context = super(MentorsPageView, self).get_context_data()

        # get user from username
        user = User.objects.get(username=self.kwargs['username'])

        # get mentor_profile
        mentor = get_object_or_404(MentorsProfile, user=user)
        context['mentor'] = mentor

        #get courses
        context['courseproductgroups'] = CourseProductGroup.objects.by_mentor(user=user)
        print context

        mentor_username = self.kwargs['username']
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
        return context