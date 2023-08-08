from django.urls import path
from . import views

urlpatterns = [
    # nombre de la url, función que devuelve, nombre para utilizarlo en los templates
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('store/',views.store, name='store'),

]
# holla

