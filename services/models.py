from django.db import models

# Create your models here.

class Service(models.Model):
    
    # Verbose_name es el nombre que aparecerá en el panel
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    # hemos definido en el setting los media_root y en imagen solo establecemos la carpeta que se crea en media
    image = models.ImageField(verbose_name='Imagen', upload_to='services')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Edición')
    
    class Meta:
        '''
        nombre en el panel
        nombre_plural en el panel
        orden de los servicio que añadiremos
        '''
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ["-created"]
        
    def __str__(self):
        return self.title