from django.contrib import admin
from .models import Partido, PerfilJugador

# Configuración pro para la lista de Partidos
class PartidoAdmin(admin.ModelAdmin):
    # Esto crea las columnas en la tabla
    list_display = ('lugar', 'fecha', 'precio', 'cupos_restantes')
    # Esto agrega un buscador por lugar
    search_fields = ('lugar',)
    # Esto agrega filtros a la derecha
    list_filter = ('fecha',)

# Registramos con la nueva configuración
admin.site.register(Partido, PartidoAdmin)
admin.site.register(PerfilJugador)