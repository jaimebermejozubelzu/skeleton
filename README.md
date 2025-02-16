# Skeleton

Skeleton es un proyecto básico, de acceso a datos con Sqlite y csv, que he tratado de modelar y refactorizar hasta alcanzar una estructura base que pueda utlizar en otros proyectos siguiendo estándares de programación en capas y DAO.

Está incompleta a propósito, solo maneja la tabla de almacenes, pudiendo listar, crear nuevos, modificar y borrar. 

## Uso

El programa consiste en una aplicación de consola que se inicia desde src/main.py

En config se puede cambiar si se desea trabajar en csv o en sqlite

## Estructura del proyecto

- `main.py` - Archivo de arranque de la aplicación en consola. Quizás sea un punto a mejorar, al no estar dentro de src, pero se me complicaba mucho la implementación
- `requirements.txt` - Archivo de requerimientos, de momento ninguno, ya que SQLite forma parte de Python.
- `.gitignore` - Para ver que no quiero subir a repositorio git
- `README.md` - Este archivo.
- `venv` (carpeta) - Para el entorno virtual (no se distribuye).
- `src` (carpeta)
  - `config.py` - Para almacenar la ruta de la base de datos, del csv y para elegir si se desea una u otra implementación de la persistencia
  - `database` (carpeta): Para almacén de datos en local.
    - `sqlite` - Para estos datos
      - `database.db` - Base de datos en formato SQLite 3.
    - `csv` - Para estos datos
      - `warehouses.csv` - Archivo csv para los datos en este formato
  - `data_layer` (carpeta): Para la capa de modelado de datos.
    - `data_entity.py` - Clase base de la que heredarán el resto de clases para el modelado de datos.
    - `models` (carpeta): En ella incluiremos todas las clases que definirán a los objetos (almacenes, productos...).
      - `warehouse.py` - Definición de la clase almacén, con propiedades y métodos específicos. Realmente no lo estoy usando, solo sería para métodos adicionales.
  - `logic_layer` (carpeta): Para la capa de lógica de negocio
    - `logic_entity.py` - Clase base de la que heredarán el resto de clases para la lógica de negocio
    - `entities` (carpeta): En ella incluiremos todas las interfaces de las entidades de negocio
      - `logic_warehouse.py` - interfaz para la capa de negocio de warehouse
  - `persistence_layer` (carpeta): Aquí se manejan los datos, en este caso sobre SQLite.
    - `persistence_entity.py` - Interfaz base para persistencia de cualquier entidadcon la base de datos (apertura, cierre, consultas).
    - `database_manager.py` - Interfaz base para manejar cualquier tipo de base de datos.
    - `csv_database_manager.py` - Clase para manejar almacenamiento en archivos CSV.
    - `sqlite_database_manager.py` - Clase para manejar SQLite.
    - `repositories` (carpeta): Código SQL puro.
      - `persistence_warehouse.py` - DAO para almacenes, heredando de PersistenceEntity
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

