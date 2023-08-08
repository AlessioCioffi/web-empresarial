from .models import Link

def dict_context(request):
    '''para que esta función devuelva un dict que pueda ser
    invocado en todas las apps añadimos esta función al sitting-templates
    en los context_processors; el archivo de la función tendrá
    el nombre de processors.py'''
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]=link.url
        '''Poniendo entonces en cualquier template el link.key,
        nos devolverá la url'''
    return ctx