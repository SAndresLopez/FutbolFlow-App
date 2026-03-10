from src.PC.Mouse import Mouse
from src.PC.Teclado import Teclado
from src.PC.Monitor import monitor


class computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor, teclado, raton):
        computadora.contador_computadora += 1
        self.id_computadora = computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return (f"{self.nombre}: {self.id_computadora}"
                f"\nMonitor: {self.monitor},"
                f"\nTeclado: {self.teclado},"
                f"\nRaton: {self.raton}")
if __name__ == "__main__":
    teclado1= Teclado("HP", "USB")
    Mouse1 = Mouse("HP", "USB")
    monitor1 = monitor("HP", 27)
    computadora1 = computadora("HP", monitor1, teclado1, Mouse1)
    print(computadora1)

    teclado2= Teclado("Gamer", "Bluetooth")
    Mouse2 = Mouse("Gamer", "Bluetooth")
    monitor2 = monitor("Gamer", 34)
    computadora2 = computadora("Gamer", monitor2, teclado2, Mouse2)
    print(computadora2)