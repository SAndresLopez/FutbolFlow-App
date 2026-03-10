from src.PC.Monitor import monitor
from src.PC.Mouse import Mouse
from src.PC.Teclado import Teclado
from src.PC.Computadora import computadora
from src.PC.orden import orden

print("PROBANDO APP")
teclado1= Teclado("HP", "USB")
Mouse1 = Mouse("HP", "USB")
monitor1 = monitor("HP", 27)
computadora1 = computadora("HP", monitor1, teclado1, Mouse1)

teclado2= Teclado("Gamer", "Bluetooth")
Mouse2 = Mouse("Gamer", "Bluetooth")
monitor2 = monitor("Gamer", 34)
computadora2 = computadora("Gamer", monitor2, teclado2, Mouse2)

computadoras1 = [computadora1, computadora2]
orden1 = orden(computadoras1)
print(orden1)