from django.shortcuts import render
from .models import Service


# Create your views here.
def services(request):
    '''
    llamamos el modelo Service para obtener todos sus objetos en 
    la variable service; esta variable service será el valor 
    en el dict de contexto en el return
    '''    
    services = Service.objects.all()
    return render(request,'services/services.html',{'services':services})