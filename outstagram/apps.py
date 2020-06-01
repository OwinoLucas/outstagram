from django.apps import AppConfig


class OutstagramConfig(AppConfig):
    name = 'outstagram'

    def ready(self):
        import outstagram.signals
