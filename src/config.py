import os

# Aquí elegimos el "motor de la base de datos"
DATABASE_TYPE = "sqlite"  # csv para CSV y sqlite para Sqlite-3
""" Vital: según lo que seleccionemos trabajará con una u otra implementación de persistencia"""

# Configuración de la base de datos
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "database", "sqlite", "database.db") 
""" Ruta de la base de datos Sqlite """

# Configuración de la carpeta para los csv
CSV_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "database", "csv")
""" Ruta del fichero csv """