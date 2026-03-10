# schemas.py
# Esquemas Pydantic para validación de datos y respuestas.

from pydantic import BaseModel, Field, field_validator
from typing import Optional

class LibroBase(BaseModel):
    """
    Esquema base con campos comunes a creación y actualización.
    Incluye validaciones de datos.
    """
    titulo: str = Field(..., min_length=1, description="Título del libro")
    autor: str = Field(..., min_length=1, description="Autor del libro")
    rating: int = Field(
        ..., ge=1, le=5,
        description="Calificación del 1 al 5"
    )

    # Validación adicional opcional

    @field_validator("titulo", "autor")
    def no_vacios(cls, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacío")

        return valor


class LibroCreate(LibroBase):
    """
    Esquema para crear un libro.
    Hereda validaciones de LibroBase.
    """
    pass

class LibroUpdate(BaseModel):
    """
    Esquema para actualizar un libro.
    Permite que los campos sean opcionales.
    """
    titulo: Optional[str] = Field(None, min_length=1)
    autor: Optional[str] = Field(None, min_length=1)
    rating: Optional[int] = Field(None, ge=1, le=5)

    @field_validator("titulo", "autor")
    def no_vacios_opcional(cls, valor):
        if valor is not None and not valor.strip():
            raise ValueError("El campo no puede estar vacío")
        return valor

class LibroRead(BaseModel):
    """
    Esquema para las respuestas del API.
    Incluye el ID del libro.
    """
    id: int
    titulo: str
    autor: str
    rating: int

    #Permite devolver objetos ORM directamente
    model_config = {
        "from_attributes": True
    }

