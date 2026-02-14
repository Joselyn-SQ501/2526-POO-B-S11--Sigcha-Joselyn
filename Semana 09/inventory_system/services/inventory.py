# Trae el modelo o clase de productos
from model.product import Product

# Clase inventario de servicio que gestiona los productos
class Inventory:
    # Creación de un constructor vacío
    def __init__(self):
        self.__products = [] # Lista principal donde se almacenan los productos

    # Método que añade un producto
    def add_product(self, product):
        # Bucle for que recorre la lista de productos para verificar si el ID del nuevo producto ya existe
        for existing_product in self.__products:
            # Condicional que compara el ID del producto existente con el ID del nuevo producto, si son iguales, se retorna False para indicar que no se puede añadir
            if existing_product.get_product_id() == product.get_product_id():
                return False
        # Si el ID no está repetido, se añade el producto a la lista
        self.__products.append(product)
        return True

    # Método que elimina un producto por su ID
    def remove_product(self, product_id: str):
        # Bucle for que recorre la lista de productos para encontrar el producto con el ID especificado
        for product in self.__products:
            # Condicional que compara el ID del producto con el ID proporcionado, si son iguales, se elimina el producto de la lista
                self.__products.remove(product)
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

        return True # Indica que se actualizó correctamente el producto
    
    # Método que lista todos los productos en el inventario
    def list_products(self):
        return self.__products
