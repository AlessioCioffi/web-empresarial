from django.shortcuts import render, get_object_or_404
from .models import Category, Post
# Create your views here.

'''Creo 2 vistas para consultar todos los posts
   y otra para consultar los post que tengan la 
   categoría requerida'''


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html',{'posts':posts})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # Con la siguiente linea obtengo los post según su categoría (funcionalidad de django)
    posts = category.post_set.all()
    return render(request, 'blog/category.html', {'category':category, 'posts':posts})

