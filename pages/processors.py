from .models import Page

def dict_pages(request):

    ctx = {}
    pages = Page.objects.all()
    for page in pages:
        ctx[page.title]=page.id
        '''esta vez tenemos que entregar un dict de contesto
        dentro de un dict de contesto para recorrer el loop for
        {% for title,id in pages.items %}
        <p><a href="{% url 'page' page_id=id %}">{{ title }}</a></p>
        {% endfor %}
        '''
        
    return {'pages':ctx}