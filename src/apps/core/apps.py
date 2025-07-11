from django.apps import AppConfig

class CoreConfig(AppConfig):
    name  = 'apps.core'
    label = 'apps_core'

    def ready(self):
        import apps.core.signals
