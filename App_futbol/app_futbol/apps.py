from django.apps import AppConfig

class AppFutbolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_futbol'

    def ready(self):

        import app_futbol.signals