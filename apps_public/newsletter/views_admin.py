# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, FormView, DetailView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.urlresolvers import reverse_lazy
from .models import Newsletter
from .forms import NewsletterEditForm

logger = logging.getLogger(__name__)

class NewsletterAdminMixin(LoginRequiredMixin,StaffuserRequiredMixin):
    pass

class NewsletterAdminListView(NewsletterAdminMixin, ListView):
    model = Newsletter
    template_name = 'newsletter/admin/index.html'
    queryset = Newsletter.objects.all()
    context_object_name = 'newsletters'
    paginate_by = 2


class NewsletterCreateView(NewsletterAdminMixin, CreateView):
    model = Newsletter
    form_class = NewsletterEditForm
    context_object_name = 'newsletter'
    template_name = 'newsletter/admin/create.html'


class NewsletterUpdateView(NewsletterAdminMixin, UpdateView):
    model = Newsletter
    template_name = 'newsletter/admin/update.html'
    context_object_name = 'newsletter'
    form_class = NewsletterEditForm


class NewsletterDeleteView(NewsletterAdminMixin, UpdateView):
    success_url = reverse_lazy('admin')
    template_name = 'newsletter/admin/delete.html'
    context_object_name = 'newsletter'
    model = Newsletter

