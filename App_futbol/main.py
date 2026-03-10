from Usuarios import Jugador
from cancha import Partido
from Seguridad import SistemaSeguridad, Reporte

# 1. El dueño crea el evento
partido_noche = Partido("20:00", 10)

# 2. Se inscriben los jugadores
andres = Jugador("Andres", 22, "A")
rival = Jugador("Rival", 25, "B")
partido_noche.inscribir_jugador(andres)
partido_noche.inscribir_jugador(rival)

# 3. Sucede un problema y alguien reporta
# (Emisor, Receptor, Categoría, Gravedad, Comentario)
nuevo_reporte = Reporte(rival, andres, "No_Pago", 5, "Se fue sin pagar su parte de la cancha")

# 4. El Administrador (tu amigo) revisa y ejecuta
print(SistemaSeguridad.ejecutar_veredicto(nuevo_reporte, es_real=True))

# 5. Ver cómo quedó el ranking
print(f"Nuevo ranking de {andres.nombre}: {andres.ranking}")