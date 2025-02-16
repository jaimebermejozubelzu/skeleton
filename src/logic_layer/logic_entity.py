from abc import ABC, abstractmethod

class LogicEntityInterface(ABC):
    """Interfaz para la lógica de negocio de cualquier entidad."""
    
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
    def select_by_criteria(self, criteria):
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

class LogicEntity(LogicEntityInterface):
    """Clase base para la lógica de negocio de cualquier entidad."""
    
    def __init__(self, persistence):
        self.persistence = persistence  # Inyectamos el DAO correspondiente

    def create(self, name):
        try:
            return self.persistence.create(name)
        except Exception as e:
            print(f"Error al crear entidad: {e}")
        return None

    def select_all(self):
        return self.persistence.select_all()

    def select_by_id(self, id):
        return self.persistence.select_by_id(id)

    def select_by_criteria(self, criteria):
        return self.persistence.select_by_criteria(criteria)

    def update(self, id, new_name):
        return self.persistence.update(id, new_name)

    def delete(self, id):
        return self.persistence.delete(id)

    def delete_all(self):
        return self.persistence.delete_all()

    def count(self):
        return self.persistence.count()

    def exists(self, id):
        return self.persistence.exists(id)

    def create_many(self, names: list):
        return self.persistence.create_many(names)