import sqlite3
import os
from config import DATABASE_PATH

class DatabaseManager:
    """Clase para manejar la conexión con SQLite."""

    def __init__(self, db_path=DATABASE_PATH):
        """Inicializa el administrador de la base de datos con una ruta."""
        self.db_path = db_path
        self._ensure_database_exists()

    def _ensure_database_exists(self):
        """Crea la base de datos si no existe."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def execute_query(self, query, params=()):
        """Ejecuta una consulta SQL de modificación (INSERT, UPDATE, DELETE)."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

    def fetch_query(self, query, params=()):
        """Ejecuta una consulta SQL de lectura (SELECT) y devuelve los resultados."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()