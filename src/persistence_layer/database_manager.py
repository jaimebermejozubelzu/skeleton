from abc import ABC, abstractmethod

class DatabaseManager(ABC):
    """Interfaz base para manejar cualquier tipo de base de datos."""

    @abstractmethod
    def insert(self, table_name, data):
        """Inserta un registro en la base de datos."""
        pass

    @abstractmethod
    def fetch_all(self, table_name):
        """Devuelve todos los registros."""
        pass

    @abstractmethod
    def fetch_by_id(self, table_name, record_id):
        """Devuelve un registro por ID."""
        pass

    @abstractmethod
    def update(self, table_name, record_id, new_data):
        """Actualiza un registro por ID."""
        pass

    @abstractmethod
    def delete(self, table_name, record_id):
        """Elimina un registro por ID."""
        pass

    @abstractmethod
    def count(self, table_name):
        """Cuenta los registros en una tabla."""
        pass
