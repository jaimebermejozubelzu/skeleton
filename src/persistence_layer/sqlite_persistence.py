from persistence_layer.persistence_entity import PersistenceEntityInterface
from persistence_layer.sqlite_database_manager import SQLiteDatabaseManager  

class SQLitePersistence(PersistenceEntityInterface):
    def __init__(self, table_name):
        self.db_manager = SQLiteDatabaseManager()
        self.table_name = table_name

    def create(self, name):
        query = f"INSERT INTO {self.table_name} (name) VALUES (?);"
        self.db_manager.execute_query(query, (name,))

    def select_all(self):
        query = f"SELECT * FROM {self.table_name};"
        return self.db_manager.fetch_query(query)

    def select_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = ?;"
        result = self.db_manager.fetch_query(query, (id,))
        return result[0] if result else None

    def select_by_criteria(self, criteria: dict):
        conditions = " AND ".join([f"{key} = ?" for key in criteria.keys()])
        query = f"SELECT * FROM {self.table_name} WHERE {conditions};"
        return self.db_manager.fetch_query(query, tuple(criteria.values()))

    def update(self, id, new_name):
        query = f"UPDATE {self.table_name} SET name = ? WHERE id = ?;"
        self.db_manager.execute_query(query, (new_name, id))

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = ?;"
        self.db_manager.execute_query(query, (id,))

    def delete_all(self):
        query = f"DELETE FROM {self.table_name};"
        self.db_manager.execute_query(query)

    def count(self):
        query = f"SELECT COUNT(*) FROM {self.table_name};"
        result = self.db_manager.fetch_query(query)
        return result[0][0] if result else 0

    def exists(self, id):
        return self.select_by_id(id) is not None

    def create_many(self, names: list):
        for name in names:
            self.create(name)