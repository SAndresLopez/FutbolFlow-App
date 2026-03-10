# Punto de entrada de la aplicación FastAPI.

from fastapi import FastAPI

# Crear instancia principal de la aplicación FastAPI.
# 'app' será utilizada por Uvicorn para levantar el servidor.
app = FastAPI(

    title="API Biblioteca Personal",
    description="Backend REST con FastAPI para gestionar libros.",
    version="1.0.0"
)
# Endpoint de prueba (ruta raíz).
# Sirve para verificar que la API está viva.

@app.get("/")
def raiz():
    """
    Endpoint básico que confirma que la API está funcionando.
    """
    return {"mensaje": "API Biblioteca funcionando correctamente"}
