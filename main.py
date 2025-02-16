import sys
import os

# Agregar `src/` al sys.path para que Python encuentre los módulos
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/src"))

from presentation_layer.presentation import ConsolePresentation
from persistence_layer.sqlite_database_manager import SQLiteDatabaseManager
from persistence_layer.csv_database_manager import CSVDatabaseManager
from persistence_layer.repositories.persistence_warehouse import PersistenceWarehouse
from config import DATABASE_TYPE

def main():
    db_manager = SQLiteDatabaseManager() if DATABASE_TYPE == "sqlite" else CSVDatabaseManager()
    
    warehouse_persistence = PersistenceWarehouse(db_manager)
 
    app = ConsolePresentation(warehouse_persistence)
    app.run()

if __name__ == "__main__":
    main()