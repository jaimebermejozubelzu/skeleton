import csv
import os
from persistence_layer.database_manager import DatabaseManager

class CSVDatabaseManager(DatabaseManager):
    """Clase para manejar almacenamiento en archivos CSV."""

    def __init__(self, folder_path="src/database/csv/"):
        """Define la carpeta donde se guardarán los CSVs."""
        self.folder_path = folder_path
        os.makedirs(folder_path, exist_ok=True)

    def _get_file_path(self, table_name):
        """Devuelve la ruta del archivo CSV correspondiente a la 'tabla'."""
        return os.path.join(self.folder_path, f"{table_name}.csv")

    def insert(self, table_name, data):
        """Inserta un registro en un archivo CSV asegurando que el encabezado incluya 'id'."""
        file_path = self._get_file_path(table_name)
        file_exists = os.path.exists(file_path)

        # Asegurar que los datos tienen 'id'
        if "id" not in data:
            data["id"] = self._generate_id(file_path)

        with open(file_path, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name"])
            if not file_exists:
                writer.writeheader()  # Escribe encabezado si el archivo es nuevo
            writer.writerow(data)

    def fetch_all(self, table_name):
        """Devuelve todos los registros de un archivo CSV."""
        file_path = self._get_file_path(table_name)
        if not os.path.exists(file_path):
            return []

        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def fetch_by_id(self, table_name, record_id):
        """Devuelve un registro por ID en un archivo CSV."""
        records = self.fetch_all(table_name)
        for record in records:
            if str(record["id"]) == str(record_id):
                return record
        return None

    def update(self, table_name, record_id, new_data):
        """Actualiza un registro en un archivo CSV."""
        file_path = self._get_file_path(table_name)
        records = self.fetch_all(table_name)

        if not records:
            return False  # No hay registros para actualizar

        # Verificar que el archivo tiene 'id'
        for record in records:
            if "id" not in record:
                raise KeyError(f"El archivo CSV '{file_path}' no contiene la clave 'id'. Verifica su estructura.")

        fieldnames = records[0].keys()  # Asegura que todos los campos originales estén presentes

        updated = False
        with open(file_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                if str(record["id"]) == str(record_id):
                    record.update(new_data)  # Solo actualiza los campos específicos
                    updated = True
                writer.writerow(record)

        return updated

    def delete(self, table_name, record_id):
        """Elimina un registro en un archivo CSV."""
        file_path = self._get_file_path(table_name)
        records = self.fetch_all(table_name)

        new_records = [r for r in records if str(r["id"]) != str(record_id)]

        with open(file_path, mode="w", newline="") as file:
            if new_records:
                writer = csv.DictWriter(file, fieldnames=new_records[0].keys())
                writer.writeheader()
                writer.writerows(new_records)

    def count(self, table_name):
        """Cuenta los registros en un archivo CSV."""
        return len(self.fetch_all(table_name))

    def _generate_id(self, file_path):
        """Genera un ID único basado en el número de filas existentes."""
        if not os.path.exists(file_path):
            return 1  # Si el archivo no existe, el primer ID será 1

        with open(file_path, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            ids = [int(row["id"]) for row in reader if "id" in row and row["id"].isdigit()]

        return max(ids) + 1 if ids else 1  # Genera un nuevo ID incremental
