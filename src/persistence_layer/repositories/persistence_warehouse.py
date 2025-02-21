from persistence_layer.persistence_entity import PersistenceEntityInterface
from persistence_layer.persistence_factory import get_persistence_driver

class PersistenceWarehouse(PersistenceEntityInterface):
    def __init__(self):
        self.driver = get_persistence_driver("warehouses")

    def create(self, name):
        self.driver.create(name)

    def select_all(self):
        return self.driver.select_all()

    def select_by_id(self, id):
        return self.driver.select_by_id(id)

    def select_by_criteria(self, criteria: dict):
        return self.driver.select_by_criteria(criteria)

    def update(self, id, new_name):
        self.driver.update(id, new_name)

    def delete(self, id):
        self.driver.delete(id)

    def delete_all(self):
        self.driver.delete_all()

    def count(self):
        return self.driver.count()

    def exists(self, id):
        return self.driver.exists(id)

    def create_many(self, names: list):
        self.driver.create_many(names)
