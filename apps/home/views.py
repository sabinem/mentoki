from django.views.generic import TemplateView
from .mixins import PublicMixin

class HomePageView(TemplateView):
    template_name = "public/homepage/homepage.html"

class TeachPageView(TemplateView):
    template_name = "public/teachpage/teach.html"

    def get_context_data(self, **kwargs):
        context = super(TeachPageView, self).get_context_data(**kwargs)
        try:
            if kwargs['goto'] == "testimonials":
                context['gotodiv']="testimonial_pagemark"
            elif kwargs['goto'] == "details":
                context['gotodiv']="detail_pagemark"
            elif kwargs['goto'] == "webinar":
                context['gotodiv']="webinar_pagemark"
        except:
            pass
        return context


class ImpressumPageView(TemplateView):
    template_name = "public/generalpages/impressum.html"

class TeamPageView(TemplateView):
    template_name = "public/generalpages/team.html"

class WebinarView(TemplateView):
    template_name = "public/webinar.html"

class NewsLetterView(TemplateView):
    template_name = "public/newsletter.html"
