from django.apps import AppConfig


class StripConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sandbox.strip'

    def ready(self):
        import sandbox.strip.signals
