import mysql.connector
from mysql.connector import pooling

# Configuramos el Pool (el estanque de conexiones)
db_config = {
    "database": "app_futbol_db",
    "user": "root",
    "password": "123456", # Cambia esto por el tuyo
    "host": "localhost"
}

try:
    # Creamos el pool con un tamaño de 5 conexiones constantes
    connection_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="futbol_pool",
        pool_size=5,
        **db_config
    )
    print("Pool de conexiones listo.")
except mysql.connector.Error as err:
    print(f"Error al crear el pool: {err}")

def crear_conexion():
    """Pide una conexión prestada al Pool"""
    try:
        # En lugar de connect(), pedimos una del estanque
        return connection_pool.get_connection()
    except mysql.connector.Error as err:
        print(f"No hay conexiones disponibles: {err}")
        return None