from abc import ABC, abstractmethod
from logic_layer.entities.logic_warehouse import LogicWarehouse

class PresentationInterface(ABC):
    @abstractmethod
    def run(self):
        pass

class ConsolePresentation(PresentationInterface):
    def __init__(self, warehouse_persistence):
        self.logic = warehouse_persistence
    
    def run(self):
        while True:
            print("\n1. Agregar almacén")
            print("2. Listar almacenes")
            print("3. Actualizar almacén")
            print("4. Eliminar almacén")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                name = input("Nombre del almacén: ")
                self.logic.create(name)
                print("Almacén agregado.")
            elif opcion == "2":
                warehouses = self.logic.select_all()
                for warehouse in warehouses:
                    print(warehouse)
            elif opcion == "3":
                id = int(input("ID del almacén: "))
                new_name = input("Nuevo nombre: ")
                if self.logic.update(id, new_name):
                    print("Almacén actualizado.")
                else:
                    print("Almacén no encontrado.")
            elif opcion == "4":
                id = int(input("ID del almacén: "))
                self.logic.delete(id)
                print("Almacén eliminado.")
            elif opcion == "5":
                break
            else:
                print("Opción no válida.") # Cambio
