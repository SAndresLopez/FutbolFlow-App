class monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        monitor.contador_monitores += 1
        self.id_monitor = monitor.contador_monitores
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f"Id: {self.id_monitor}, Marca: {self.marca},"
                f"Tamanio: {self.tamanio}")

if __name__ == '__main__':
    monitor1 = monitor("HP", 15)
    print(monitor1)
    monitor2 = monitor("Dell", 27)
    print(monitor2)