print("*** Leer archivos ***")

nombre_archivo = "mi_archivo.txt"

with open(nombre_archivo, "r") as archivo:
    print(archivo.readlines())
with open(nombre_archivo, "r") as archivo:
    print(archivo.read().strip())