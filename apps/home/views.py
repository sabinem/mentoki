from django.views.generic import TemplateView
from .mixins import PublicMixin


class HomePageView(PublicMixin, TemplateView):
    template_name = "public/homepage.html"


class StarterkursPageView(PublicMixin, TemplateView):
    template_name = "public/starterkurs.html"


class ImpressumPageView(PublicMixin, TemplateView):
    template_name = "public/impressum.html"


class TeamPageView(PublicMixin, TemplateView):
    template_name = "public/team.html"