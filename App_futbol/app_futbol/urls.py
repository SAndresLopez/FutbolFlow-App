from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('unirse/<int:partido_id>/', views.unirse_partido, name='unirse_partido'),
    path('completar-perfil/', views.completar_perfil, name='completar_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('partido/<int:partido_id>/elegir_formacion/', views.elegir_formacion, name='elegir_formacion'),
    path('partido/<int:partido_id>/inscribirse/<str:equipo>/<int:pos_num>/',
         views.inscribirse,
         name='inscribirse'),
    path('partido/<int:partido_id>/eliminar_inscripcion/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
    path('reportar/', views.enviar_reporte, name='enviar_reporte')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)