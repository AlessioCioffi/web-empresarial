from django.shortcuts import render,HttpResponse


# Create your views here.

'''
HttpRestonse devuelve directamente la palabra 'inicio' 
en la pagina indicada en el request

def home(request): 
    return HttpResponse('Inicio')
'''

def home(request):
    # Render devuelve a la request la conexión al templates
    return render(request,'core/home.html')


def about(request):
    return render(request,'core/about.html')


def store(request):
    return render(request,'core/store.html')
