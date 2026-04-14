class Mensaje:
    def __init__(self, autor, contenido):
        self.autor_nombre = autor.nombre
        self.equipo = autor.equipo
        self.contenido = contenido

class SalaChat:
    def __init__(self, partido_id):
        self.partido_id = partido_id
        self.mensajes_equipo_a = []
        self.mensajes_equipo_b = []

    def enviar_mensaje(self, jugador_emisor, texto):
        nuevo_msj = Mensaje(jugador_emisor, texto)

        if jugador_emisor.equipo == "A":
            self.mensajes_equipo_a.append(nuevo_msj)
            return "Enviado al Equipo A"
        else:
            self.mensajes_equipo_b.append(nuevo_msj)
            return "Enviado al Equipo B"