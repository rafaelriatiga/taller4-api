"""
ingesta.py
Consumo de la API pública DummyJSON y almacenamiento de datos crudos en MongoDB.

Flujo:
    1. Extracción: descarga el catálogo completo de productos desde la API.
    2. Carga: inserta los registros sin transformar en la colección raw_data.
"""

import requests
from pymongo import MongoClient

# Endpoint de productos. limit=0 retorna el catálogo completo en una sola petición.
API_URL = "https://dummyjson.com/products?limit=0"

# Parámetros de conexión a la instancia local de MongoDB.
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "taller4_db"
COLLECTION_NAME = "raw_data"


def extraer_productos(url):
    """Solicita los productos a la API y retorna la lista de registros."""
    respuesta = requests.get(url)
    respuesta.raise_for_status()  # Detiene la ejecución si la API responde con error.
    return respuesta.json()["products"]


def cargar_en_mongodb(productos, uri, db_name, collection_name):
    """Inserta los registros en MongoDB y retorna la cantidad insertada."""
    cliente = MongoClient(uri)
    coleccion = cliente[db_name][collection_name]

    # Vacía la colección antes de insertar para garantizar idempotencia
    # (re-ejecutar el script no genera documentos duplicados).
    coleccion.delete_many({})

    resultado = coleccion.insert_many(productos)
    return len(resultado.inserted_ids)


def main():
    productos = extraer_productos(API_URL)
    print(f"Productos descargados: {len(productos)}")

    insertados = cargar_en_mongodb(productos, MONGO_URI, DB_NAME, COLLECTION_NAME)
    print(f"Documentos insertados en {DB_NAME}.{COLLECTION_NAME}: {insertados}")


if __name__ == "__main__":
    main()