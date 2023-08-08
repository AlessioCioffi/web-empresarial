from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Page(models.Model):
    
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Edición')
    
    class Meta:
        '''
        nombre en el panel
        nombre_plural en el panel
        orden de los servicio que añadiremos
        '''
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ["-title"]
        
    def __str__(self):
        return self.title