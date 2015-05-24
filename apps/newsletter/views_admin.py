import logging
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, FormView
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from .models import Newsletter
from .forms import NewsletterCreateForm, NewsletterUpdateForm


logger = logging.getLogger(__name__)

class NewsletterAdminListView(ListView):
    model = Newsletter
    template_name = 'newsletter/admin/newsletter_list.html'
    queryset = Newsletter.objects.published()
    context_object_name = 'newsletters'
    paginate_by = 2

class NewsletterCreateView(CreateView):
    model = Newsletter
    form_class = NewsletterCreateForm
    template_name = 'newsletter/admin/newsletter_create.html'


class NewsletterUpdateView(FormView):

    form_class = NewsletterUpdateForm
    template_name = 'newsletter/admin/newsletter_update.html'

