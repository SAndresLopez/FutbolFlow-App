from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('unirse/<int:partido_id>/', views.unirse_partido, name='unirse_partido'),
    path('completar-perfil/', views.completar_perfil, name='completar_perfil'),
]