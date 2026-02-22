# Permite trabajar con rutas y archivos del sistema
import os
# Trae el modelo o clase de productos
from model.product import Product

# Clase inventario de servicio que gestiona los productos
class Inventory:
    # Constructor de la clase vacío
    def __init__(self):
        self.__products = [] # Lista principal donde se almacenan los productos
        self.__file_name = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "inventario.txt"
        )  # Ruta para que el archivo se cree dentro de la carpeta correspondiente
        self.load_from_file()  # Carga automáticamente los productos al iniciar el programa

    # Método para guardar en un archivo
    def save_to_file(self):
        try:
            # Abre el archivo en modo escritura ("w") y si no existe, lo crea automáticamente
            with open(self.__file_name, "w", encoding="utf-8") as file:
                # Recorre la lista de productos en memoria
                for product in self.__products:
                    # Crea una línea en formato CSV separado por comas
                    line = f"{product.get_product_id()},{product.get_name()},{product.get_quantity()},{product.get_price()}\n"
                    # Escribe la línea en el archivo
                    file.write(line)

            return True  # Indica que se guardó correctamente

        # Se ejecuta si el sistema no tiene permisos para escribir
        except PermissionError:
            print("✖️ Error: No se tienen permisos para escribir en el archivo.")
            return False

        # Captura cualquier otro error inesperado
        except Exception as e:
            print(f"⚠ Error inesperado al guardar el archivo: {e}")
            return False

    # Método para cargar desde un archivo
    def load_from_file(self):
        try:
            # Abre el archivo en modo lectura
            with open(self.__file_name, "r", encoding="utf-8") as file:
                # Permite llevar conteo del número de línea
                for line_number, line in enumerate(file, start=1):

                    # Si la línea está vacía, la ignora
                    if not line.strip():
                        continue

                    # Divide la línea por comas
                    data = line.strip().split(",")

                    # Si la línea no tiene exactamente 4 datos, la ignora
                    if len(data) != 4:
                        continue

                    # Asigna cada valor a su variable correspondiente
                    product_id, name, quantity, price = data

                    try:
                        # Crea un objeto Product convirtiendo cantidad y precio a tipos numéricos
                        product = Product(
                            product_id,
                            name,
                            int(quantity),  # Convierte a entero
                            float(price)  # Convierte a decimal
                        )

                        # Agrega el producto a la lista en memoria
                        self.__products.append(product)

                    except ValueError:
                        # Si hay error en conversión de datos (datos corruptos)
                        print(f"⚠ Línea {line_number} ignorada: datos corruptos")
                        continue

        # Si el archivo no existe, lo crea vacío
        except FileNotFoundError:
            open(self.__file_name, "w").close()
            print("📁 Archivo inventario.txt creado automáticamente.")

        # Si no hay permisos para leer el archivo
        except PermissionError:
            print("✖️ Error: No se tienen permisos para leer el archivo.")

        # Captura cualquier otro error inesperado
        except Exception as e:
            print(f"⚠ Error inesperado al cargar el archivo: {e}")

    # Método que añade un producto
    def add_product(self, product):
        # Bucle for que recorre la lista de productos para verificar si el ID del nuevo producto ya existe
        for existing_product in self.__products:
            # Condicional que compara el ID del producto existente con el ID del nuevo producto, si son iguales, se retorna False para indicar que no se puede añadir
            if existing_product.get_product_id() == product.get_product_id():
                return False
        # Si el ID no está repetido, se añade el producto a la lista
        self.__products.append(product)

        # Guarda automáticamente en el archivo
        save_add = self.save_to_file()
        if not save_add:
            self.__products.remove(product)
            return False

        return True

    # Método que elimina un producto por su ID
    def remove_product(self, product_id: str):
        # Bucle for que recorre la lista de productos para encontrar el producto con el ID especificado
        for product in self.__products:
            # Condicional que compara el ID del producto con el ID proporcionado, si son iguales, se elimina el producto de la lista
            if product.get_product_id() == product_id:
                self.__products.remove(product)

                # Guarda cambios en el archivo
                save_remove = self.save_to_file()

                # Si hubo error al guardar, revierte el cambio
                if not save_remove:
                    self.__products.append(product)
                    return False

                return True # Indica que se eliminó correctamente el producto
        return False # Si no se encuentra el producto con el ID especificado no se elimina el producto

    # Método que busca productos por su ID
    def find_by_id(self, product_id: str):
        # Bucle for que recorre la lista de productos para encontrar el producto con el ID especificado
        for product in self.__products:
            # Condicional que compara el ID del producto con el ID proporcionado, si son iguales, se retorna el producto encontrado
            if product.get_product_id() == product_id:
                return product
        return None # Si no se encuentra el producto con el ID especificado, se retorna que no se encontró el producto

    # Método que busca productos por su nombre
    def find_by_name(self, name: str):
        # Bucle for que recorre la lista de productos para encontrar los productos que contienen el nombre especificado (permitiendo coincidencias parciales)
        results = []
        # Bucle for que recorre la lista de productos para comparar el nombre del producto con el nombre proporcionado, si son iguales incluso parcialmente, se añade el producto a la lista de resultados
        for product in self.__products:
            if name.lower() in product.get_name().lower(): # Condicional que permite coincidencias parciales y no distingue entre mayúsculas y minúsculas
                results.append(product)
        return results

    # Método que actualiza la cantidad o precio de un producto por su ID
    def update_product(self, product_id: str, quantity: int = None, price: float = None):
        product = self.find_by_id(product_id) # Llama al método find_by_id para encontrar el producto con el ID especificado

        if not product:
            return False  # Si no se encuentra el producto con el ID especificado, se retorna que no se pudo actualizar
        
        # Condicional que verifica si se proporcionó una nueva cantidad, si es así, se actualiza la cantidad del producto por el método setter correspondiente
        if quantity is not None:
            product.set_quantity(quantity)

        # Condicional que verifica si se proporcionó un nuevo precio, si es así, se actualiza el precio del producto por el método setter correspondiente
        if price is not None:
            product.set_price(price)

        # Guarda cambios en archivo (reescribe el inventario)
        save_update = self.save_to_file()
        if not save_update:
            return False

        return True # Indica que se actualizó correctamente el producto
    
    # Método que lista todos los productos en el inventario
    def list_products(self):
        return self.__products
