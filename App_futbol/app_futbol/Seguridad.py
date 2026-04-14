class Reporte:
    def __init__(self, emisor, receptor, categoria, gravedad, comentario=""):
        self.emisor = emisor
        self.receptor = receptor
        self.categoria = categoria
        self.gravedad = gravedad  # 1-5
        self.comentario = comentario
        self.estado = "Pendiente"

class SistemaSeguridad:
    @staticmethod
    def ejecutar_veredicto(reporte, es_real):
        """Procesa reportes negativos y fake reports."""
        if es_real:
            puntos_a_restar = reporte.gravedad * 0.4
            reporte.receptor.ranking -= puntos_a_restar
            if reporte.receptor.ranking < 0: reporte.receptor.ranking = 0.0
            return f"PENALIZACIÓN: {reporte.receptor.nombre} perdió {puntos_a_restar:.1f} pts por {reporte.categoria}."
        else:
            reporte.emisor.ranking -= 1.5
            if reporte.emisor.ranking < 0: reporte.emisor.ranking = 0.0
            return f"FAKE REPORT: {reporte.emisor.nombre} penalizado con -1.5 pts por mentir."

    @staticmethod
    def premiar_jugador(receptor, motivo):
        """Sube el ranking por buen comportamiento o MVP."""
        puntos_a_subir = 0.2
        ranking_previo = receptor.ranking
        receptor.ranking += puntos_a_subir

        if receptor.ranking > 5.0:
            receptor.ranking = 5.0

        return (f"PREMIO: {receptor.nombre} recibió +{puntos_a_subir} pts por {motivo}.\n"
                f"Ranking: {ranking_previo:.1f} -> {receptor.ranking:.1f}")

    @staticmethod
    def generar_ranking_top(lista_jugadores):
        return sorted(lista_jugadores, key=lambda j: j.ranking, reverse=True)

def limpiar_texto(texto_sucio):
    if not texto_sucio:
        return ""

    palabras_prohibidas = ['aborto', 'Aborto', 'estafa']

    texto_limpio = texto_sucio
    for palabra in palabras_prohibidas:
        texto_limpio = texto_limpio.replace(palabra, "***")

    import re
    texto_limpio = re.sub('<[^<]+?>', '', texto_limpio)

    return texto_limpio