nombre_archivo = ("mi_archivo.txt")
with open(nombre_archivo, "w") as archivo:
    archivo.write("Hola, como estas?")
    archivo.write("\nagregando informacion")

print(f"se creo el archivo: {nombre_archivo}")