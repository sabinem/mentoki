import logging
from django.core.urlresolvers import resolve



logger = logging.getLogger(__name__)


MATCH_URL_NAMES_BUILDLESSON = ["buildlessons",
                               "updatematerial"]


class MatchMixin(object):
    """
    this mixin just tries to get the url data. They are needed to display the menu
    and the actives links in the correct was
    """
    def get_context_data(self, **kwargs):
        context = super(MatchMixin, self).get_context_data(**kwargs)
        try :
            match = resolve(self.request.path)
        except:
            match = None
        context['match'] = match
        if match.namespace in ["home","public"]:
            context['section'] = "front"
        elif match.namespace == "course":
            context['section'] = "course"
        elif match.namespace == "desk":
            context['section'] = "desk"
        elif match.namespace == "buildclassroom":
            context['section'] = "classroombackend"
        elif match.namespace == "classroom":
            context['section'] = "classroom"
        elif match.namespace == "forum":
            context['section'] = "classroom"
        logger.debug("---------- in matchmixin url_name = %s namespace = %s" % (match.url_name, match.namespace))
        print match
        return context
