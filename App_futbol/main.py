from Usuarios import Jugador
from gestor_partidos import GestorPartidos

def pantalla_inicio():
    print("\n" + "=" * 40)
    print("Bienvenido A TU APP DE FÚTBOL ")
    print("=" * 40)
    print("Iniciando sesión con Google...")

    # Simulación de Login con Gmail
    email = input("Introduce tu Gmail para entrar: ").lower().strip()

    # Buscamos al jugador en la DB por su email
    jugador_actual = Jugador.buscar_por_email(email)

    if not jugador_actual:
        print("\nParece que es tu primera vez. ¡Regístrate!")
        nombre = input("¿Cómo te llamas en la cancha?: ")
        edad = int(input("¿Qué edad tienes?: "))
        # Lo creamos en la DB
        jugador_actual = Jugador(nombre, email, edad, "S/N")
        jugador_actual.guardar_en_db()
        print(f"¡Perfil creado con éxito, {nombre}!")
    else:
        print(f"\n¡Qué bueno verte de nuevo, {jugador_actual.nombre}!")
        print(f"Tu Ranking actual es: {jugador_actual.ranking}")

    return jugador_actual


def menu_principal(usuario):
    while True:
        print("\n" + "-" * 30)
        print(f"PERFIL: {usuario.nombre} | {usuario.email}")
        print("-" * 30)
        print("1. Ver Partidos Disponibles")
        print("2. Ver mi Alineación (Estilo FIFA)")
        print("3. Inscribirme a un Partido")
        print("4. MI PERFIL (Estadísticas)")
        print("5. RANKING GLOBAL (Top 10)")
        print("0. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            print("\n--- PRÓXIMOS ENCUENTROS ---")
            GestorPartidos.ver_partidos_disponibles()

        elif opcion == "2":
            id_p = int(input("ID del partido para ver la táctica: "))
            GestorPartidos.ver_alineacion_fifa(id_p)

        elif opcion == "3":
            print("\n--- INSCRIPCIÓN TÁCTICA ---")
            id_p = int(input("ID del Partido al que te quieres unir: "))

            # Primero le mostramos cómo va la cancha para que elija bien
            GestorPartidos.ver_alineacion_fifa(id_p)

            print("\nPosiciones: Portero, Defensa, Mediocampista, Delantero")
            pos = input("¿En qué posición quieres jugar?: ")
            eq = input("¿Equipo A o B?: ").upper()

            # Usamos el id_jugador que obtuvimos en el login
            GestorPartidos.unirse_a_posicion(usuario.id_jugador, id_p, eq, pos)

        elif opcion == "4":
            # Llamamos a la función pro que acabamos de crear
            Jugador.obtener_perfil_completo(usuario.email)

        elif opcion == "5":
            Jugador.ver_top_jugadores()

        elif opcion == "0":
            print("¡Nos vemos en los vestuarios!")
            break


if __name__ == "__main__":
    # 1. Login Primero
    user_logueado = pantalla_inicio()
    # 2. Si el login fue exitoso, entramos al menú
    if user_logueado:
        menu_principal(user_logueado)