import sqlite3
import os
from config import DATABASE_PATH
from persistence_layer.database_manager import DatabaseManager

class SQLiteDatabaseManager(DatabaseManager):
    """Clase para manejar SQLite."""

    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = db_path
        self._ensure_database_exists()

    def _ensure_database_exists(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

    def execute_query(self, query, params=()):
        """Ejecuta una consulta SQL de modificación."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()

    def fetch_query(self, query, params=()):
        """Ejecuta una consulta SQL de lectura."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def insert(self, table_name, data):
        """Inserta un registro en una tabla SQLite."""
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(data.values()))

    def fetch_all(self, table_name):
        """Devuelve todos los registros de una tabla SQLite."""
        query = f"SELECT * FROM {table_name}"
        return self.fetch_query(query)

    def fetch_by_id(self, table_name, record_id):
        """Devuelve un registro por ID en SQLite."""
        query = f"SELECT * FROM {table_name} WHERE id = ?"
        result = self.fetch_query(query, (record_id,))
        return result[0] if result else None

    def update(self, table_name, record_id, new_data):
        """Actualiza un registro en SQLite."""
        columns = ', '.join([f"{key} = ?" for key in new_data.keys()])
        query = f"UPDATE {table_name} SET {columns} WHERE id = ?"
        self.execute_query(query, tuple(new_data.values()) + (record_id,))

    def delete(self, table_name, record_id):
        """Elimina un registro en SQLite."""
        query = f"DELETE FROM {table_name} WHERE id = ?"
        self.execute_query(query, (record_id,))

    def count(self, table_name):
        """Cuenta los registros en una tabla SQLite."""
        query = f"SELECT COUNT(*) FROM {table_name}"
        result = self.fetch_query(query)
        return result[0][0] if result else 0
