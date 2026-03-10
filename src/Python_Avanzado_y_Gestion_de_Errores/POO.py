#Prueba N°1, conectar una clase_objeto con MySQL
import mysql.connector

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def Definir(self):
        return (f"Hola, soy: {self.nombre}"
                f"\nmi contacto es: {self.email}")

try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="blogdb"
    )
    cursor = conexion.cursor()
    nombre1 = input("Ingrese su nombre: ")
    email1 = input("Ingrese su email: ")
    usuario1 = Usuario(nombre1, email1)

    print(usuario1.Definir())

    sql = "insert into usuarios_test(nombre, email) values (%s, %s)"
    valores = (usuario1.nombre, usuario1.email)

    cursor.execute(sql,valores)
    conexion.commit()
    print("usuario guardado en MySQL")
except Exception as e:
        print(f"Error {e}")
finally:
        if conexion in locals() and conexion.is_connected():
            cursor.close()
            conexion.close()
#Tuve problemas en la creacion de este archivo
#Errores en la indentación del código, asi como en
#los nombres de las variables, a futuro tratar de no comenterlos
#El codigo está corregido sin embargo hay que pulir unas cosas.