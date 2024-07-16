from django.apps import AppConfig

class AuthConfig(AppConfig):
    # Set the default auto field to use for models in this application
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Name of the application
    name = 'authcart'
