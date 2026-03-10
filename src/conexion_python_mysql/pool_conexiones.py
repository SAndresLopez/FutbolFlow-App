from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    database ="blogdb"
    username ="root"
    password = "******"
    host ="localhost"
    port = 3306 #puerto por defecto
    pool_size = 5 #cantidad de objetos
    pool_name ="plantilla de un pool de conexiones" #nombre del pool
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.pool_name,
                    pool_size = cls.pool_size,
                    host = cls.host,
                    port = cls.port,
                    database = cls.database,
                    user = cls.username,
                    password = cls.password
                )
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al obtener pool: {e}")
        else:
            return cls.pool
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls,conexion):
        conexion.close()

if __name__ == "__main__":
    pool = Conexion.obtener_pool()
    print(pool)