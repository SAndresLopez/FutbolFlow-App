# database.py
# Configuración de la base de datos, sesión y prueba de conexión.

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()
# Construcción de la URL de conexión a MySQL
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
 f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Creación del motor de conexión
engine = create_engine(
    DATABASE_URL,
    echo=False # Cambiar a True si quieres ver las consultas SQL
)

# Crear un SessionLocal por petición
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para los modelos
Base = declarative_base()


# Dependencia para FastAPI: obtiene una sesión por petición y la cierra
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Prueba rápida de conexión: ejecutar con "python database.py"
if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Conexión exitosa a MySQL")
    except Exception as e:
        print("Error al conectar a la base de datos:", e)