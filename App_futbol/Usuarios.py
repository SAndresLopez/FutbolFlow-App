from conexion_db import crear_conexion

class Jugador:
    def __init__(self, nombre, edad, email, equipo,id_jugador=None, ranking=5.0, es_admin=False):
        self.id_jugador = id_jugador
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.es_admin = es_admin
        self.equipo = equipo  # "A" o "B"
        self.ranking = 5.0    # Puntaje inicial
        self.esta_pagado = False
        self.es_titular = False
        self.reportes_recibidos = []

    def guardar_en_db(self):
        """Inserta este objeto Jugador en la tabla de MySQL"""
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Usamos el nombre exacto de tus columnas: id_jugador, nombre, edad, equipo, ranking
                sql = "INSERT INTO jugadores (nombre, edad, equipo, ranking) VALUES (%s, %s, %s, %s)"
                valores = (self.nombre, self.edad, self.equipo, self.ranking)

                cursor.execute(sql, valores)
                conexion.commit()

                # Seteamos el id que nos dio la base de datos
                self.id_jugador = cursor.lastrowid
                print(f"{self.nombre} guardado en DB con ID: {self.id_jugador}")

            except Exception as e:
                print(f"Error al guardar: {e}")
            finally:
                conexion.close()

    @staticmethod
    def cargar_todos_de_db():
        conexion = crear_conexion()
        lista_jugadores = []
        if conexion:
            try:
                # Usamos dictionary=True para leer por nombre de columna (más seguro)
                cursor = conexion.cursor(dictionary=True)
                cursor.execute("SELECT * FROM jugadores")
                for r in cursor.fetchall():
                    # Creamos el objeto Jugador con los datos de la fila
                    j = Jugador(r['nombre'], r['edad'], r['equipo'], r['id_jugador'], r['ranking'])
                    lista_jugadores.append(j)
            finally:
                conexion.close()
        return lista_jugadores

    def __str__(self):
        rol = "Titular" if self.es_titular else "Suplente"
        pago = "Pagado" if self.esta_pagado else "Pendiente"
        return f"[{self.equipo}] {self.nombre}, {self.ranking:.1f}, {rol}, {pago}"

    @staticmethod
    def buscar_o_registrar_por_email(email, nombre_google):
        conexion = crear_conexion()
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM jugadores WHERE email = %s", (email,))
            usuario = cursor.fetchone()

            if usuario:
                print(f"Bienvenido de nuevo, {usuario['nombre']}")
                return Jugador(usuario['nombre'], usuario['email'], usuario['edad'], usuario['equipo'],
                               usuario['id_jugador'], usuario['ranking'])
            else:
                print("Primera vez con Gmail. Creando perfil...")
                edad = int(input("¿Cuántos años tienes? "))
                nuevo = Jugador(nombre_google, email, edad, "S/N")
                nuevo.guardar_en_db()
                return nuevo

    @staticmethod
    def buscar_por_email(email):
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return None
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM jugadores WHERE email = %s", (email,))
            u = cursor.fetchone()
            if u:
                return Jugador(u['nombre'], u['email'], u['edad'], u['equipo'], u['id_jugador'], u['ranking'])
            return None
        finally:
            conexion.close()

    @staticmethod
    def actualizar_ranking(id_jugador, nueva_nota):
        """Fórmula de Media Ponderada Profesional"""
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)
            #Obtenemos datos actuales
            cursor.execute("SELECT ranking, partidos_jugados FROM jugadores WHERE id_jugador = %s", (id_jugador,))
            datos = cursor.fetchone()

            rank_actual = float(datos['ranking'])
            pj = datos['partidos_jugados']

            #Aplicamos la fórmula pro
            nuevo_ranking = ((rank_actual * pj) + nueva_nota) / (pj + 1)
            nuevo_ranking = round(nuevo_ranking, 2)

            #Actualizamos ranking Y sumamos un partido jugado
            sql = "UPDATE jugadores SET ranking = %s, partidos_jugados = partidos_jugados + 1 WHERE id_jugador = %s"
            cursor.execute(sql, (nuevo_ranking, id_jugador))
            conexion.commit()

            print(f"PJ: {pj + 1} | Nuevo Ranking: {nuevo_ranking}")
        finally:
            conexion.close()

    @staticmethod
    def obtener_perfil_completo(email):
        """Consulta toda la data del jugador para el menú lateral"""
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)
            sql = "SELECT nombre, ranking, partidos_jugados, equipo FROM jugadores WHERE email = %s"
            cursor.execute(sql, (email,))
            d = cursor.fetchone()

            if d:
                # Lógica de categorías estilo FIFA
                rank = float(d['ranking'])
                pj = d['partidos_jugados']

                if pj < 5:
                    categoria = "NOVATO"
                elif rank >= 4.5:
                    categoria = "LEYENDA"
                elif rank >= 3.5:
                    categoria = "PROMESA"
                else:
                    categoria = "AMATEUR"

                print("\n" + "╔" + "═" * 38 + "╗")
                print(f"║ PERFIL DE JUGADOR: {d['nombre'].upper().center(18)} ║")
                print("╠" + "═" * 38 + "╣")
                print(f"║  Categoría: {categoria.ljust(24)} ║")
                print(f"║  Ranking:   {'⭐' * int(rank)} ({rank:.2f})".ljust(40) + "║")
                print(f"║  Partidos:  {str(pj).ljust(24)} ║")
                print(f"║  Equipo:    {d['equipo'].ljust(24)} ║")
                print("╚" + "═" * 38 + "╝")
            else:
                print("Jugador no encontrado.")
        finally:
            conexion.close()

    @staticmethod
    def ver_top_jugadores():
        """Muestra a los 10 mejores jugadores de la app"""
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)
            # Solo mostramos a los que tengan al menos 3 partidos jugados
            sql = """
                    SELECT nombre, ranking, partidos_jugados 
                    FROM jugadores 
                    WHERE partidos_jugados >= 3 
                    ORDER BY ranking DESC LIMIT 10
                """
            cursor.execute(sql)
            tops = cursor.fetchall()

            print("\n" + "🏆" + "—" * 35 + "🏆")
            print("      RANKING GLOBAL - TOP 10")
            print("—" * 39)

            for i, j in enumerate(tops, 1):
                medalla = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f" {i}."
                print(f"{medalla} {j['nombre'].ljust(15)} | {j['ranking']} | {j['partidos_jugados']} PJ")

            print("—" * 39)
        finally:
            conexion.close()