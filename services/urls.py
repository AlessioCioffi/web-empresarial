from django.urls import path
from .views import services
from services import views
urlpatterns = [
    path('',views.services, name='services')
]
