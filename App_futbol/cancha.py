class Partido:
    def __init__(self, hora, capacidad):
        self.hora = hora
        self.capacidad = capacidad
        self.titulares = []
        self.suplentes = []

    def inscribir_jugador(self, jugador):
        if len(self.titulares) < self.capacidad:
            jugador.es_titular = True
            # Por defecto, al inscribirse como titular, debe pagar
            jugador.esta_pagado = False
            self.titulares.append(jugador)
            return f"{jugador.nombre} reservó a las {self.hora} (Titular)"
        else:
            jugador.es_titular = False
            jugador.esta_pagado = False # Suplentes no pagan hasta que suban a titulares
            self.suplentes.append(jugador)
            return f"{self.hora} LLENO. {jugador.nombre} a lista de espera."

    def obtener_todos(self):
        return self.titulares + self.suplentes