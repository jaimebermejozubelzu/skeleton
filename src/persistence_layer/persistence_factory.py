from .csv_persistence import CSVPersistence
from .sqlite_persistence import SQLitePersistence
from config import DATABASE_TYPE

def get_persistence_driver(table_name):
    if DATABASE_TYPE == "csv":
        return CSVPersistence(table_name)
    elif DATABASE_TYPE == "sqlite":
        return SQLitePersistence(table_name)
    else:
        raise ValueError(f"Tipo de persistencia no soportado: {DATABASE_TYPE}")