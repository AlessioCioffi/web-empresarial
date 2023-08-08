from django.db import models

# Create your models here.
class ClientData(models.Model):
    
    name = models.CharField(max_length=200, verbose_name='Nombre')
    email = models.EmailField(max_length=200, verbose_name='Correo')
    
    class Meta:
        
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        
    def __str__(self):
        return self.name
    