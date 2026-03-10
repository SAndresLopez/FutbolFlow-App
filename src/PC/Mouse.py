from src.PC.entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):
    contador_mouse = 0

    def __init__(self, marca, tipo_entrada):
        Mouse.contador_mouse += 1
        self.id_raton = Mouse.contador_mouse
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'Id:{self.id_raton}, Marca: {self.tipo_entrada}, '
                f'tipo de entrada: {self.tipo_entrada}')
if __name__ == "__main__":
    Mouse1 = Mouse("Xiaomi","bluetooth")
    print(Mouse1)
    Mouse2 = Mouse("Samsung","USB")
    print(Mouse2)
