from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Newsletter

class LatestNewsletterFeed(Feed):
    title = "Mentokis Newsletters"
    link = "/feed/"
    description = "Monthly Newsletter for Mentoki."

    def items(self):
        return Newsletter.objects.published()[:1]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    # item_link is only needed if NewsItem has no get_absolute_url method.
