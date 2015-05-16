import logging
from django.views.generic import TemplateView, CreateView, UpdateView
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from .models import Newsletter
from .forms import NewsletterCreateForm, NewsletterUpdateForm


logger = logging.getLogger(__name__)


class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterCreateForm
    template_name = 'newslettercreate.html'


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    form_class = NewsletterUpdateForm
    template_name = 'newsletterupdate.html'

