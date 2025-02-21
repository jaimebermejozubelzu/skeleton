from persistence_layer.persistence_entity import PersistenceEntityInterface
from persistence_layer.csv_database_manager import CSVDatabaseManager  

class CSVPersistence(PersistenceEntityInterface):
    def __init__(self, table_name):
        self.db_manager = CSVDatabaseManager()
        self.table_name = table_name

    def create(self, name):
        data = {"id": self.count() + 1, "name": name}
        self.db_manager.insert(self.table_name, data)

    def select_all(self):
        return self.db_manager.fetch_all(self.table_name)

    def select_by_id(self, id):
        records = self.db_manager.fetch_all(self.table_name)
        return next((r for r in records if str(r["id"]) == str(id)), None)

    def select_by_criteria(self, criteria: dict):
        records = self.db_manager.fetch_all(self.table_name)
        for key, value in criteria.items():
            records = [r for r in records if r.get(key) == value]
        return records

    def update(self, id, new_name):
        self.db_manager.update(self.table_name, id, {"name": new_name})

    def delete(self, id):
        self.db_manager.delete(self.table_name, id)

    def delete_all(self):
        self.db_manager.delete_all(self.table_name)

    def count(self):
        return len(self.db_manager.fetch_all(self.table_name))

    def exists(self, id):
        return self.select_by_id(id) is not None

    def create_many(self, names: list):
        for name in names:
            self.create(name)