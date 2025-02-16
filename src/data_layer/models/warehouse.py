from data_layer.data_entity import Entity

class Warehouse(Entity):
    """Representa un almacén."""

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Almacén ({self.id}, {self.name})"
    
    def __eq__(self, other):
        """Compara dos almacenes por su nombre e ID."""
        if not isinstance(other, Warehouse):
            return False
        return self.name == other.name and self.id == other.id
    
    def __str__(self):
        return f"Almacén ID {self.id}: {self.name}"

    def get_key(self):
        """Devuelve la clave única para el almacén."""
        return {"name": self.name}

    @staticmethod
    def from_dict(dicted_entity: dict):
        """Construye una instancia de Warehouse desde un diccionario."""
        return Warehouse(**dicted_entity)
    
    def to_dict(self):
        """Convierte la instancia de Warehouse en un diccionario."""
        return {
            "_id": self.id,
            "name": self.name
        }