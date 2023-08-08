from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    # nombre de la app en el panel y so config en el setting
    verbose_name ='Gestor de servicios'
