from django.contrib import admin
from .models import Partido, PerfilJugador,Inscripcion
class PartidoAdmin(admin.ModelAdmin):
    list_display = ('lugar', 'fecha', 'precio', 'cupos_restantes')
    search_fields = ('lugar',)
    list_filter = ('fecha',)

admin.site.register(Partido, PartidoAdmin)
admin.site.register(PerfilJugador)
admin.site.register(Inscripcion)