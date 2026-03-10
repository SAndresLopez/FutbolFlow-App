print("*** Decorador ***")

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de llamar a saludar")
        resultado = funcion(*args, **kwargs)
        print("Despues de llamar a saludar")
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f"Hola {nombre}")
saludar("Andres")