from django.core.urlresolvers import resolve

class PublicMixin(object):

    def get_context_data(self, **kwargs):
        context = super(PublicMixin, self).get_context_data(**kwargs)
        try :
            match = resolve(self.request.path)
        except:
            match = None
        context['match']= match

        return context