class orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        orden.contador_ordenes += 1
        self.id_orden = orden.contador_ordenes
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ""
        for computadora in self.computadoras:
            computadoras_str += f" \n" +computadora.__str__()
        return (f"orden {self.id_orden} "
                f"\n Computadoras: {computadoras_str}")