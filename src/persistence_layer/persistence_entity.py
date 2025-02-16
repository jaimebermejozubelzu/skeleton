from abc import ABC, abstractmethod
from persistence_layer.database_manager import DatabaseManager

class PersistenceEntityInterface(ABC):
    """Interfaz base para persistencia de cualquier entidad."""
    
    @abstractmethod
    def create(self, name):
        pass

    @abstractmethod
    def select_all(self):
        pass

    @abstractmethod
    def select_by_id(self, id):
        pass

    @abstractmethod
    def select_by_criteria(self, criteria: dict):
        pass

    @abstractmethod
    def update(self, id, new_name):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def count(self):
        pass

    @abstractmethod
    def exists(self, id):
        pass

    @abstractmethod
    def create_many(self, names: list):
        pass

class PersistenceEntity(PersistenceEntityInterface):
    """Clase base para persistencia en memoria de cualquier entidad."""

    def __init__(self, db_manager=None):
        """Inicializa la persistencia con un `DatabaseManager`."""
        self.db_manager = db_manager or DatabaseManager()
        self.table_name = None  # Debe ser definido en la subclase

    def select_all(self):
        """Obtiene todas las filas de la tabla específica."""
        query = f"SELECT * FROM {self.table_name};"
        return self.db_manager.fetch_query(query)

    def select_by_id(self, id):
        """Obtiene una fila por su ID."""
        query = f"SELECT * FROM {self.table_name} WHERE id = ?;"
        result = self.db_manager.fetch_query(query, (id,))
        return result[0] if result else None

    def delete(self, id):
        """Elimina una fila por su ID."""
        query = f"DELETE FROM {self.table_name} WHERE id = ?;"
        self.db_manager.execute_query(query, (id,))

    def delete_all(self):
        """Elimina todas las filas de la tabla."""
        query = f"DELETE FROM {self.table_name};"
        self.db_manager.execute_query(query)

    def count(self):
        """Cuenta cuántos registros hay en la tabla."""
        query = f"SELECT COUNT(*) FROM {self.table_name};"
        result = self.db_manager.fetch_query(query)
        return result[0][0] if result else 0

    def create_many(self, names: list):
        """Inserta múltiples registros en la tabla."""
        query = f"INSERT INTO {self.table_name} (name) VALUES (?);"
        for name in names:
            self.db_manager.execute_query(query, (name,))
        return True

    def create(self, name):
        """Inserta un nuevo registro en la tabla."""
        query = f"INSERT INTO {self.table_name} (name) VALUES (?);"
        self.db_manager.execute_query(query, (name,))
        return True

    def exists(self, id):
        """Verifica si un registro existe en la tabla."""
        return self.select_by_id(id) is not None

    def select_by_criteria(self, criteria: dict):
        """Obtiene registros que cumplen ciertos criterios."""
        conditions = " AND ".join([f"{key} = ?" for key in criteria.keys()])
        query = f"SELECT * FROM {self.table_name} WHERE {conditions};"
        return self.db_manager.fetch_query(query, tuple(criteria.values()))

    def update(self, id, new_name):
        """Actualiza el nombre de un registro."""
        query = f"UPDATE {self.table_name} SET name = ? WHERE id = ?;"
        self.db_manager.execute_query(query, (new_name, id))