from Usuarios import Jugador
from cancha import Partido
from Seguridad import SistemaSeguridad, generar_ranking_top

# 1. El dueño abre un partido a las 9 PM para 2 personas (prueba rápida)
partido_9pm = Partido("21:00", 2)

# 2. Llegan 3 amigos
j1 = Jugador("Andres", 22, "A")
j2 = Jugador("Socio", 23, "A")
j3 = Jugador("Rival", 24, "B")

for j in [j1, j2, j3]:
    print(partido_9pm.inscribir_jugador(j))

# 3. Simulación de conflicto: El rival reporta falsamente a Andres
print("\n--- Incidente en la cancha ---")
reporte = SistemaSeguridad.procesar_reporte(j3, j1, "Insultos", 5, False)
print(reporte)

# 4. Ver Ranking Final
print("\n--- Ranking de la App ---")
top = generar_ranking_top(partido_9pm.obtener_todos())
for i, p in enumerate(top, 1):
    print(f"{i}. {p}")