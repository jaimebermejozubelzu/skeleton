# Skeleton

Skeleton es un proyecto básico, de acceso a datos con Sqlite, que he tratado de modelar y refactorizar hasta alcanzar una estructura base que pueda utlizar en otros proyectos siguiendo estándares de programación en capas.

Está incompleta a propósito, solo maneja la tabla de almacenes, pudiendo listar, crear nuevos, modificar y borrar. 

## Uso

El programa consiste en una aplicación de consola que se inicia desde src/main.py

## Estructura del proyecto

- `requirements.txt` - Archivo de requerimientos, de momento ninguno, ya que SQLite forma parte de Python.
- `.gitignore` - Para ver que no quiero subir a repositorio git
- `README.md` - Este archivo.
- `config.py` - Para almacenar la ruta de la base de datos
- `venv` (carpeta) - Para el entorno virtual (no se distribuye).
- `src` (carpeta)
  - `main.py` - Archivo de arranque de la aplicación en consola.
  - `database` (carpeta): Para almacén de datos en local.
    - `database.db` - Base de datos en formato SQLite 3.
  - `data_layer` (carpeta): Para la capa de modelado de datos.
    - `data_entity.py` - Clase base de la que heredarán el resto de clases para el modelado de datos.
    - `models` (carpeta): En ella incluiremos todas las clases que definirán a los objetos (almacenes, productos...).
      - `warehouse.py` - Definición de la clase almacén, con propiedades y métodos específicos.
  - `persistence_layer` (carpeta): Aquí se manejan los datos, en este caso sobre SQLite.
    - `persistence_entity.py` - Métodos básicos de acceso a datos (`SELECT`, `DELETE`, etc.) y conexión con la base de datos (apertura, cierre, consultas).
    - `repositories` (carpeta): Código SQL puro.
      - `persistence_warehouse.py` - Código SQL para almacenes.
  - `presentation_layer` (carpeta): En ella establecemos toda la lógica de presentación.
    - `presentation.py` - Creación de un menú para interactuar desde la consola.

## Creación del entorno virtual

Acceder a terminal y desde el directorio base ir lanzando:

### Crear el entorno virtual
python -m venv venv

### Activar el entorno virtual en Windows
venv\Scripts\Activate

### Activar el entorno virtual en Unix/Mac
source venv/bin/activate

### Instalar librerías necesarias (en este caso, SQLite ya está incluido en Python)
pip install sqlite3  # No es necesario

