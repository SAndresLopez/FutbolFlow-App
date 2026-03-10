class Jugador:
    def __init__(self, nombre, edad, equipo):
        self.nombre = nombre
        self.edad = edad
        self.equipo = equipo  # "A" o "B"
        self.ranking = 5.0    # Puntaje inicial
        self.esta_pagado = False
        self.es_titular = False
        self.reportes_recibidos = []

    def __str__(self):
        rol = "Titular" if self.es_titular else "Suplente"
        pago = "Pagado" if self.esta_pagado else "Pendiente"
        return f"[{self.equipo}] {self.nombre}, {self.ranking:.1f}, {rol}, {pago}"

