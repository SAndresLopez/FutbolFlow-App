import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="******",
    database="blogdb"
)
cursor = conexion.cursor()
cursor.execute("SELECT * FROM usuarios_test")
resultado = cursor.fetchall()
print("\n --- LISTA DE USUARIOS DE PRUEBAS ---")
for fila in resultado:
    print(f"ID: {fila[0]} | Nombre: {fila[1]} | email: {fila[2]}")

conexion.close()