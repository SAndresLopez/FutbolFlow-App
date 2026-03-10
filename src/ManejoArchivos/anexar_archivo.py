print("*** Anexar información")

nombre_archivo = "mi_archivo.txt"
with open(nombre_archivo, "a") as archivo:
    archivo.write("\nAnexando informacion...")
    archivo.write("\nSaliendo de anexar informacion...")

print(f"Se ha anexado información al archivo {nombre_archivo}")