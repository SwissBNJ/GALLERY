import importlib
from django.apps import AppConfig


class pgsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pgsApp'

    def ready(self):
        # Importing modules dynamically using importlib
        module_name = 'some_module'  # Replace with your actual module name
        try:
            importlib.import_module(module_name)
        except ModuleNotFoundError:
            # Handle the case where the module could not be imported
            pass
