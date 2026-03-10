import mysql.connector
try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="******",
        database="blogdb"
    )
    cursor = conexion.cursor()

    nombre = input("Ingrese nombre de usuario: ")
    email = input("Ingrese su email: ")

    sql = "INSERT INTO usuarios_test (nombre, email) VALUES (%s, %s)"
    valores = (nombre, email)

    cursor.execute(sql, valores)
    conexion.commit()

    print(f"{cursor.rowcount} Usuario registrado correctamente")

except Exception as fail:
    print(f"Error:{fail}")
finally:
    if "conexion" in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()
        print(" Fin de la conexion")