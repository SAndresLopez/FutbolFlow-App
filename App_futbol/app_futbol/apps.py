from django.apps import AppConfig

class AppFutbolConfig(AppConfig):
    name = 'app_futbol'

    def ready(self):

        import app_futbol.signals