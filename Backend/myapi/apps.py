'''
API app configuration
'''
from django.apps import AppConfig

class MyapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapi'
    
    def ready(self):
        from . import startup
        startup.run_startup_check()
