import logging
from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Newsletter
from .forms import NewsletterCreateForm, NewsletterUpdateForm


logger = logging.getLogger(__name__)


class NewslettersListView(TemplateView):
    template_name = 'newsletterlist.html'

    def get_context_data(self, **kwargs):
        context = super(NewslettersListView, self).get_context_data(**kwargs)
        logger.debug("---------- in NewsletterListView get_context_data")
        newsletter_list = Newsletter.objects.filter(published=True).order_by('-published_at_date')
        context['newsletter_list'] = newsletter_list
        print context['newsletter_list']
        return context


class NewsletterDetailView(TemplateView):
    template_name = 'newsletterdetail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsletterDetailView, self).get_context_data(**kwargs)
        logger.debug("---------- in NewsletterDetailView get_context_data")
        newsletter = Newsletter.objects.get(id=self.kwargs['id'])
        context['newsletter'] = newsletter
        return context


