from django.contrib import admin
from .models import Category, Post
# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    # Clase que permite restringir a sola lectura atributos de category
    readonly_fields = ('created','updated')
    
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    # Clase que permite restringir a sola lectura atributos de post
    readonly_fields = ('created','updated')
    # Para que en el panel veamos 
    list_display = ('title','author','published')
    # ordenar por autor y luego fecha - poner siempre una coma si hay un solo elemento
    ordering = ('author','published')
    # Poner un buscador donde podamos escribir titulo o content/ ponemos author_username porque vamos a la foreign
    #search_fields = ('title','content','author_username')
    # Filtrar por nombre del user
    #list_filter = ('author_username',)
    
        
admin.site.register(Post, PostAdmin)
