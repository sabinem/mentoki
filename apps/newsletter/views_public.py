import logging
from django.views.generic import TemplateView, ListView, DetailView
from .models import Newsletter
from .forms import NewsletterCreateForm, NewsletterUpdateForm


logger = logging.getLogger(__name__)


class NewslettersListView(ListView):
    queryset = Newsletter.objects.published()
    template_name = 'newsletter/public/newsletter_list.html'
    context_object_name = 'newsletters'
    paginate_by = 2


class NewsletterDetailView(DetailView):
    model = Newsletter
    template_name = 'newsletter/public/newsletter_detail.html'



