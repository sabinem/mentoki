import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url, **kwargs):
    url = reverse(url, kwargs)
    try:
        pass
        #url = reverse(kwargs['url'] kwargs)
    except NoReverseMatch:
        #pattern = url
        pass
    path = context['request'].path
    #if re.search('a', path):
    #    return 'active'
    return url

