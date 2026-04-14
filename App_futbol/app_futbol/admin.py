from django.contrib import admin
from .models import Reporte, Partido, PerfilJugador, Inscripcion

@admin.register(Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'fecha', 'precio', 'cupos_restantes')
    search_fields = ('lugar',)
    list_filter = ('fecha',)

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('descripcion',)

@admin.register(PerfilJugador)
class PerfilJugadorAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'apodo', 'estrellas', 'puntos')
    search_fields = ('usuario__username', 'apodo')

admin.site.register(Inscripcion)