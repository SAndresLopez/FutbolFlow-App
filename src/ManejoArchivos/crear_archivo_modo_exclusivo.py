print("*** Abrir un archivo en modo exclusivo ***")
nombre_archivo = "mi_archivo_exclusivo.txt"
try:
    with open(nombre_archivo, "x") as archivo:
        archivo.write("escritura en modo exclusivo")
        archivo.write("\nEspero que sea util")
    print(f"archivo creado {nombre_archivo}")
except FileExistsError:
    print(f"El archivo {nombre_archivo} ya existe")