from django.contrib import admin
from .models import Reporte, Partido, PerfilJugador, Inscripcion

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'fecha', 'precio', 'cupos_restantes')
    search_fields = ('lugar',)
    list_filter = ('fecha',)


@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('descripcion',)

admin.site.register(Partido, PartidoAdmin)
admin.site.register(PerfilJugador)
admin.site.register(Inscripcion)