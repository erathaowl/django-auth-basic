from django.apps import AppConfig
from django.conf import settings

class CoreConfig(AppConfig):
    name = f"{settings.PROJECT_NAME}.core"
