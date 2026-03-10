# migrate.py
# Script para generar y aplicar migraciones con Alembic automáticamente.

import os
from dotenv import load_dotenv
from alembic.config import Config
from alembic import command
import pymysql

# Cargar variables del .env
load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Verificar si existe la base de datos y si existe la tabla alembic_version
def limpiar_alembic_version():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("""
            SHOW TABLES LIKE 'alembic_version';
        """)
        existe = cursor.fetchone()
        if existe:
            print("Tabla alembic_version encontrada. OK.")
        else:
            print("No existe tabla alembic_version. Continuando...")
        conn.close()
    except Exception as e:
        print("Error verificando alembic_version:", e)

# Ejecutar migración automática

def ejecutar_migracion():
    alembic_cfg = Config("alembic.ini")
    print(" Generando revisión autogenerada...")
    command.revision(alembic_cfg, autogenerate=True, message="init libros")

    print("Aplicando migración (upgrade head)...")
    command.upgrade(alembic_cfg, "head")
    print("Migración aplicada correctamente.")


if __name__ == "__main__":
 limpiar_alembic_version()
 ejecutar_migracion()
