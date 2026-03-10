from logging import exception

print("Manejo de excepciones")

def dividir (numerador, denominador):
    try:
        resultado = numerador / denominador
        print(f"Resultado de la division: {resultado}")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        print(f"Terminamos de procesar la exception")

dividir(numerador=float(input("Ingrese un numero: ")),
        denominador=float(input("Ingrese un numero: ")))

