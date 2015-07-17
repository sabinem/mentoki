import logging
from django.views.generic import TemplateView, ListView, DetailView
from .models import Newsletter


logger = logging.getLogger(__name__)


class NewsletterPublicListView(ListView):
    queryset = Newsletter.objects.published()
    template_name = 'newsletter/public/index.html'
    context_object_name = 'newsletters'
    paginate_by = 2


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'newsletter/public/detail.html'



