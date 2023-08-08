from django.contrib import admin
from .models import Service
# Register your models here.

class ServicesAdmin(admin.ModelAdmin):
    # Clase que permite restringir a sola lectura atributos de Services
    readonly_fields = ('created','updated')

# Código para registrar el modelo en en el panel de administrador
admin.site.register(Service,ServicesAdmin)

