from django.contrib import admin

from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    # Clase que permite restringir a sola lectura atributos de Pages
    readonly_fields = ('created','updated')

# Código para registrar el modelo en en el panel de administrador
admin.site.register(Page, PageAdmin)