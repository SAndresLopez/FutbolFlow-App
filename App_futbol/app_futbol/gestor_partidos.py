
from conexion_db import crear_conexion


class GestorPartidos:
    @staticmethod
    def crear_partido(fecha, hora, lugar, precio):
        """Función exclusiva para el Administrador"""
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor()
            # El estado por defecto es 'Abierto'
            sql = "INSERT INTO partidos (fecha, hora, lugar, precio, estado) VALUES (%s, %s, %s, %s, 'Abierto')"
            cursor.execute(sql, (fecha, hora, lugar, precio))
            conexion.commit()

            print(f"\n¡NUEVA CONVOCATORIA CREADA!")
            print(f"Lugar: {lugar} |  {fecha} a las {hora} |  Precio: {precio}")
        except Exception as e:
            print(f"Error al crear el evento: {e}")
        finally:
            conexion.close()

    @staticmethod
    def unirse_a_equipo(id_jugador, id_partido, equipo_elegido):
        """
        Permite a un jugador unirse a un equipo (A o B) validando:
        1. Que el equipo exista.
        2. Que no haya más de 5 personas en ese equipo.
        """
        equipo_elegido = equipo_elegido.upper()

        if equipo_elegido not in ['A', 'B']:
            print("Equipo no válido. Elige A o B.")
            return

        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)

            # 1. Validar cuántos hay en ese equipo específico para ese partido
            sql_conteo = "SELECT COUNT(*) as total FROM inscripciones WHERE id_partido = %s AND equipo_asignado = %s"
            cursor.execute(sql_conteo, (id_partido, equipo_elegido))
            jugadores_en_equipo = cursor.fetchone()['total']

            # 2. Regla de negocio: Máximo 5 por bando para un 5v5
            if jugadores_en_equipo >= 5:
                print(f"El Equipo {equipo_elegido} ya está lleno (5/5). ¡Prueba en el otro!")
                return

            # 3. Registrar la inscripción en MySQL
            sql_insert = "INSERT INTO inscripciones (id_partido, id_jugador, equipo_asignado) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert, (id_partido, id_jugador, equipo_elegido))
            conexion.commit()

            print(f"¡Éxito! Jugador ID {id_jugador} unido al Equipo {equipo_elegido} para el Partido {id_partido}.")

        except Exception as e:
            print(f"Error al procesar la inscripción: {e}")
        finally:
            conexion.close()

    @staticmethod
    def ver_convocatoria(id_partido):
        """
        Muestra la lista de jugadores inscritos divididos por equipos.
        """
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)
            # Hacemos un JOIN para traer el NOMBRE del jugador desde la tabla jugadores
            sql = """
                SELECT j.nombre, i.equipo_asignado, j.ranking 
                FROM inscripciones i 
                JOIN jugadores j ON i.id_jugador = j.id_jugador 
                WHERE i.id_partido = %s
                ORDER BY i.equipo_asignado ASC
            """
            cursor.execute(sql, (id_partido,))
            jugadores = cursor.fetchall()

            print(f"\n--- CONVOCATORIA PARTIDO #{id_partido} ---")
            if not jugadores:
                print("Aún no hay nadie inscrito. ¡Sé el primero!")
            else:
                for j in jugadores:
                    print(f"[{j['equipo_asignado']}] {j['nombre']} (Rank: {j['ranking']})")

        except Exception as e:
            print(f"Error al consultar la lista: {e}")
        finally:
            conexion.close()

    @staticmethod
    def ver_partidos_disponibles():
        """
        Consulta la tabla 'partidos' para ver qué hay programado.
        """
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)
            # Unimos con 'canchas' para saber el nombre del lugar
            sql = """
                    SELECT p.id_partido, c.nombre as cancha, p.fecha, p.hora_inicio, p.estado 
                    FROM partidos p
                    JOIN canchas c ON p.id_cancha = c.id_cancha
                    WHERE p.estado = 'Abierto'
                """
            cursor.execute(sql)
            partidos = cursor.fetchall()

            print("\n--- PARTIDOS DISPONIBLES ---")
            for p in partidos:
                print(f"ID: {p['id_partido']} | {p['cancha']} | {p['fecha']} @ {p['hora_inicio']}")
        finally:
            conexion.close()

    @staticmethod
    def unirse_a_posicion(id_jugador, id_partido, equipo, posicion):
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return False

        try:
            cursor = conexion.cursor(dictionary=True)

            cursor.execute("SELECT COUNT(*) as total FROM inscripciones WHERE id_partido = %s", (id_partido,))
            conteo = cursor.fetchone()['total']

            limite_cupos = 12

            if conteo >= limite_cupos:
                print(f"\n¡LO SIENTO! El partido ya está lleno ({conteo}/{limite_cupos}).")
                return False

            sql_pos = "SELECT * FROM inscripciones WHERE id_partido = %s AND equipo_asignado = %s AND posicion = %s"
            cursor.execute(sql_pos, (id_partido, equipo, posicion))
            if cursor.fetchone():
                print(f"La posición {posicion} en el Equipo {equipo} ya está tomada.")
                return False

            sql_ins = "INSERT INTO inscripciones (id_jugador, id_partido, equipo_asignado, posicion) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_ins, (id_jugador, id_partido, equipo, posicion))
            conexion.commit()
            print(f"¡Inscripción exitosa! Te vemos en la cancha como {posicion}.")
            return True

        finally:
            conexion.close()

    @staticmethod
    def ver_alineacion_fifa(id_partido):
        """Muestra la formación táctica del partido estilo FIFA"""
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor(dictionary=True)
            # Traemos a todos los inscritos con su nombre y posición
            sql = """
                SELECT j.nombre, i.equipo_asignado, i.posicion, i.pagado 
                FROM inscripciones i 
                JOIN jugadores j ON i.id_jugador = j.id_jugador 
                WHERE i.id_partido = %s
                """
            cursor.execute(sql, (id_partido,))
            jugadores = cursor.fetchall()

            equipos = {'A': {}, 'B': {}}
            posiciones_estandar = ['Portero', 'Defensa', 'Mediocampista', 'Delantero']

            for j in jugadores:
                equipos[j['equipo_asignado']][j['posicion']] = j['nombre']

            print(f"\n{'=' * 20} ESTRATEGIA DEL ENCUENTRO {'=' * 20}")

            for eq in ['A', 'B']:
                print(f"\nEQUIPO {eq}:")
                for pos in posiciones_estandar:
                    ocupante = equipos[eq].get(pos, "--- VACANTE ---")
                    print(f"  [{pos.ljust(13)}]: {ocupante}")

            print("\n" + "=" * 50)

        except Exception as e:
            print(f"Error al cargar la táctica: {e}")
        finally:
            conexion.close()

    @staticmethod
    def registrar_pago(id_jugador, id_partido):
        """Marca la inscripción de un jugador como pagada"""
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return

        try:
            cursor = conexion.cursor()
            sql = "UPDATE inscripciones SET pagado = TRUE WHERE id_jugador = %s AND id_partido = %s"
            cursor.execute(sql, (id_jugador, id_partido))
            conexion.commit()

            if cursor.rowcount > 0:
                print(f"¡Pago confirmado para el jugador {id_jugador}!")
            else:
                print("No se encontró la inscripción para este pago.")
        finally:
            conexion.close()

    @staticmethod
    def generar_reporte_caja(id_partido):
        """Muestra el estado financiero de un partido específico"""
        from conexion_db import crear_conexion
        conexion = crear_conexion()
        if not conexion: return False

        try:
            cursor = conexion.cursor(dictionary=True)

            # 1. Traemos datos del partido (Precio y Lugar)
            cursor.execute("SELECT lugar, precio FROM partidos WHERE id_partido = %s", (id_partido,))
            partido = cursor.fetchone()

            if not partido:
                print("El partido no existe.")
                return False

            precio_cuota = partido['precio']

            # 2. Contamos cuántos han pagado y cuántos faltan
            sql_stats = """
                    SELECT 
                        COUNT(*) as total_inscritos,
                        SUM(CASE WHEN pagado = 1 THEN 1 ELSE 0 END) as han_pagado,
                        SUM(CASE WHEN pagado = 0 THEN 1 ELSE 0 END) as morosos
                    FROM inscripciones WHERE id_partido = %s
                """
            cursor.execute(sql_stats, (id_partido,))
            stats = cursor.fetchone()

            total_recaudado = stats['han_pagado'] * precio_cuota
            total_pendiente = stats['morosos'] * precio_cuota

            # --- DISEÑO DEL REPORTE ---
            print("\n" + "💵" + "—" * 35 + "💵")
            print(f"      REPORTE DE CAJA - ID: {id_partido}")
            print(f"      📍 {partido['lugar']}")
            print("—" * 39)
            print(f"✅ PAGADOS:    {stats['han_pagado']} jugadores  -> S/. {total_recaudado:.2f}")
            print(f"❌ DEUDORES:   {stats['morosos']} jugadores  -> S/. {total_pendiente:.2f}")
            print("—" * 39)
            print(f"TOTAL EN CAJA ACTUAL:      S/. {total_recaudado:.2f}")
            print(f"TOTAL ESPERADO (FULL):     S/. {total_recaudado + total_pendiente:.2f}")
            print("—" * 39)

        finally:
            conexion.close()
