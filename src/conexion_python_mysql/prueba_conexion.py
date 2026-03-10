import mysql.connector

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='******',
        database='blogdb'
    )
    if conexion.is_connected():
        print("Conectado a blogdb")
        conexion.close()
except Exception as fail:
    print(f"Error:{fail}")