# Taller 4 — APIs Públicas, MongoDB y EDA

Proyecto del curso **Bases de Datos para Ciencia de Datos** (Universidad de Antioquia).
Simula un flujo de Ciencia de Datos de extremo a extremo: extracción de datos desde una
API pública, almacenamiento crudo en MongoDB (NoSQL) y análisis exploratorio (EDA) en
Jupyter Notebook.

**Autor:** Rafael Alexander Riatiga Duran

## API utilizada

[**DummyJSON**](https://dummyjson.com/products) — API pública y gratuita que provee un
catálogo de productos de e-commerce simulado. Se consume el endpoint
`https://dummyjson.com/products?limit=0`, que retorna el catálogo completo (194 productos)
en una sola petición.

Cada producto incluye campos como `title`, `category`, `price`, `rating`, `stock`,
`brand`, entre otros.

## Estructura del proyecto

```
.
├── ingesta.py          # Script de extracción (API) y carga (MongoDB)
├── analisis.ipynb      # Notebook con el análisis exploratorio (EDA)
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Exclusiones de Git (entorno virtual, temporales)
└── README.md           # Este archivo
```

## Flujo del proyecto

1. **Extracción:** `ingesta.py` descarga los productos desde la API de DummyJSON.
2. **Almacenamiento:** los registros se insertan sin modificar en MongoDB, en la base de
   datos `taller4_db` y la colección `raw_data`.
3. **Análisis (EDA):** `analisis.ipynb` se conecta a MongoDB, carga los datos en un
   DataFrame de pandas, selecciona 5 variables relevantes y genera insights numéricos y
   visualizaciones.

## Requisitos previos

- Python 3.10 o superior
- MongoDB Community Server instalado y corriendo localmente (puerto por defecto `27017`)
- Jupyter Notebook (incluido en las dependencias)

## Cómo ejecutarlo

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/rafaelriatiga/taller4-api.git
   cd taller4-api
   ```

2. **Crear y activar un entorno virtual:**

   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. **Instalar las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el script de ingesta** (descarga los datos y los guarda en MongoDB):

   ```bash
   python ingesta.py
   ```

5. **Abrir el notebook de análisis:**

   Abrir `analisis.ipynb` en Jupyter o en VS Code y ejecutar todas las celdas en orden.

## Análisis realizado

El notebook incluye:

- **Selección de variables:** `title`, `category`, `price`, `rating`, `stock`.
- **Inspección básica:** primeras filas (`head`), tipos de datos (`info`) y verificación
  de valores nulos.
- **5 insights numéricos:** precio promedio, rango de precios (producto más caro y más
  barato), número de categorías y la más numerosa, rating promedio y producto mejor
  calificado, e inventario total.
- **3 visualizaciones:** gráfico de torta (distribución por categoría), gráfico de barras
  (top 10 categorías) e histograma (distribución de ratings).

## Tecnologías

- **Python** — lenguaje principal
- **requests** — consumo de la API
- **pymongo** — conexión con MongoDB
- **pandas** — manipulación y análisis de datos
- **matplotlib** — visualizaciones
- **MongoDB** — almacenamiento NoSQL
