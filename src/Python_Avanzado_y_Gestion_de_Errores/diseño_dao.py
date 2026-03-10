
class disenoDAO:
    seleccionar = "select * from cliente order id"
    insertar = "insert into cliente (nombre, apellido, membresia) values (%s, %s, %s)"
    actualizar = "update cliente set nombre = %s, apellido = %s, membresia = %s where id = %s"
    eliminar = "delete from cliente where id = %s"

    @classmethod
    def seleccionar (cls):
        conexion = None
        try:
        except Exception as e:
            print(f"ocurrio un error al seleccionar un cliente: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                conexion.liberar_conexion(conexion)
