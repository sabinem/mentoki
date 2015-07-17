from django.db.models.query import QuerySet


class NewsletterQuerySet(QuerySet):
    """
    all published newsletters
    """
    def published(self):
        return self.filter(published=True)
