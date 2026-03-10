class Reporte:
    def __init__(self, emisor, receptor, categoria, gravedad, comentario=""):
        # Categorías sugeridas: "Violencia", "Falta_Asistencia", "No_Pago", "Conducta_Antideportiva"
        self.emisor = emisor
        self.receptor = receptor
        self.categoria = categoria
        self.gravedad = gravedad  # Escala 1-5
        self.comentario = comentario  # El texto opcional del usuario
        self.estado = "Pendiente"  # Esperando revisión del admin

class SistemaSeguridad:
    @staticmethod
    def ejecutar_veredicto(reporte, es_real, puntos_manuales=None):
        if es_real:
            # Si el admin NO pone puntos manuales, usa la fórmula (gravedad * 0.4)
            if puntos_manuales is None:
                puntos_a_restar = reporte.gravedad * 0.4
            else:
                # Si el admin decide poner un número específico, se usa ese
                puntos_a_restar = puntos_manuales

            reporte.receptor.ranking -= puntos_a_restar

            # Limitar a que el ranking no sea menor a 0
            if reporte.receptor.ranking < 0: reporte.receptor.ranking = 0

            return f"Veredicto: Se restaron {puntos_a_restar:.1f} puntos a {reporte.receptor.nombre}."

        else:
            reporte.estado = "Rechazado"
            # Se resta ranking al EMISOR por mentiroso
            reporte.emisor.ranking -= 2.0
            if reporte.emisor.ranking < 0: reporte.emisor.ranking = 0

            return f"Se ha penalizado a {reporte.emisor.nombre} por reporte falso."

    @staticmethod
    def validar_chat(j1, j2):
        if j1.equipo == j2.equipo:
            return True
        return False