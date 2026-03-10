class Persona:
    def __init__(self, nombre, Apellido, edad):
        self.nombre = nombre
        self.Apellido = Apellido
        self.edad = edad
    def mostrar_persona(self):
        print(f" nombre: {self.nombre}"
              f"\n Apellido: {self.Apellido}"
              f"\n edad: {self.edad}")

if __name__ == '__main__':
    persona1= Persona("Andres", "Lopez", 18)
    persona1.mostrar_persona()
    persona2= Persona("Melissa", "Lopez", 24)
    persona2.mostrar_persona()
    persona3= Persona("Xiomara", "Jimenez", 24)
    persona3.mostrar_persona()
