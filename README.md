# ImplementationPylintBlack
Repo for Implementation Pylint and Black in FastAPI

## Requisitos
- Python 3.x
- Docker

## Instalación
1. Clonar el repositorio.
2. Crear un archivo `.env` con las variables de entorno necesarias.
3. Ejecutar `docker-compose up -d` para levantar la base de datos.
4. Instalar las dependencias: `pip install -r requirements.txt`.

## Ejecutar la aplicación
- Iniciar el servidor FastAPI: `uvicorn app.main --reload`

## Ejecutar Pylint
- Ejecutar `pylint app/` para analizar la calidad del código.
