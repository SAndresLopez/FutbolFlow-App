class Aritmetica():
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        return print(f" La suma: {resultado}")
    def resta(self):
        resultado = self.operando1 - self.operando2
        return print(f" La resta: {resultado}")
    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        return print(f" La multiplicacion: {resultado}")
    def dividir(self):
        resultado = self.operando1 / self.operando2
        return print(f" La division: {resultado}")
if __name__ == '__main__':
    print("*** Ejmplo de aritmetica con clases ***")
    aritmetica1 =Aritmetica(operando1=float(input("Introduce un numero: ")),
                            operando2=float(input("Introduce un numero: ")))
    aritmetica1.sumar()
    aritmetica1.resta()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
