def obtener_ranking_global(lista_jugadores):
    jugadores_validos = [j for j in lista_jugadores if hasattr(j, 'ranking')]

    # Ordenamos de mayor a menor
    return sorted(jugadores_validos, key=lambda j: j.ranking, reverse=True)

def imprimir_tabla(lista_ordenada):
    print("\n--- TABLA DE POSICIONES ---")
    for pos, j in enumerate(lista_ordenada, 1):
        print(f"{pos}. {j.nombre} | {j.ranking:.1f}")