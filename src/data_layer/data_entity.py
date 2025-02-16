from abc import ABC, abstractmethod

class Entity(ABC):
    """Clase base para todas las entidades del sistema."""

    @abstractmethod
    def from_dict(self, dicted_entity: dict):
        """Método para construir una entidad a partir de un diccionario."""
        pass

    @abstractmethod
    def to_dict(self):
        """Convierte la entidad en un diccionario."""
        pass