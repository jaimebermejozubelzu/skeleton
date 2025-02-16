from persistence_layer.persistence_entity import PersistenceEntity

class PersistenceWarehouse(PersistenceEntity):
    """DAO para almacenes, heredando de PersistenceEntity."""
    
    def __init__(self, db_manager=None):
        super().__init__(db_manager)
        self.table_name = "warehouses"

    def create_table(self):
        """Crea la tabla de almacenes si no existe."""
        query = """
        CREATE TABLE IF NOT EXISTS warehouses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        """
        self.db_manager.execute_query(query)