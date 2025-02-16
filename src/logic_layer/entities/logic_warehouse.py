from abc import ABC, abstractmethod
from persistence_layer.repositories.persistence_warehouse import PersistenceWarehouse
from logic_layer.logic_entity import LogicEntity

class LogicWarehouseInterface(ABC):
    """Interfaz para la lógica de negocio específica de almacenes."""
    
    @abstractmethod
    def fake(self):
        """Método ficticio que devuelve un valor nulo."""
        pass

class LogicWarehouse(LogicEntity, LogicWarehouseInterface):
    def __init__(self):
        super().__init__(PersistenceWarehouse())
    
    def fake(self):
        """Método ficticio que devuelve None."""
        return None
   