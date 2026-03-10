# models/libro.py
# Definición del modelo Libro para la base de datos.
from sqlalchemy import Column, Integer, String
from database import Base
class Libro(Base):
    """
    Modelo SQLAlchemy que representa la tabla 'libros'.
    Cada atributo corresponde a una columna en la base de datos.
    """
    __tablename__ = "libros"

    # ID autoincremental y llave primaria
    id = Column(Integer, primary_key=True, autoincrement=True)

    # Título del libro (cadena obligatoria)
    titulo = Column(String(255), nullable=False)

    # Autor del libro (cadena obligatoria)
    autor = Column(String(255), nullable=False)

    # Rating entre 1 y 5 (entero obligatorio)
    rating = Column(Integer, nullable=False)