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