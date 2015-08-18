from django.apps import AppConfig

class CourseEventConfig(AppConfig):
    name = 'apps_data.courseevent'
    verbose_name = 'courseevent'

    def ready(self):
        import apps_data.courseevent.signals.handlers
