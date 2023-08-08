from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Edición')
    
    class Meta:
        '''
        nombre en el panel
        nombre_plural en el panel
        orden de los servicio que añadiremos
        '''
        verbose_name = 'categoría '
        verbose_name_plural = 'categorías'
        ordering = ["-created"]
        
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    # Puede elegir la fecha pero en default ponemos la ora actual de la zona horaria del caso
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen',upload_to='blog',null=True,blank=True)
    # Vamos a dirigirnos al id del User con la ForeignKey
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ManyToManyField(Category,verbose_name='Categoría')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Edición')
    
    class Meta:
        '''
        nombre en el panel
        nombre_plural en el panel
        orden de los servicio que añadiremos
        '''
        verbose_name = 'publicación'
        verbose_name_plural = 'publicaciones'
        ordering = ["-created"]
        
    def __str__(self):
        return self.title