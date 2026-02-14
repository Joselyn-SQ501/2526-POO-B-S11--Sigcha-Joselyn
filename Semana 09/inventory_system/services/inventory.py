# Trae el modelo o clase de productos
from model.product import Product

# Clase inventario de servicio que gestiona los productos
class Inventory:
    # Creación de un constructor vacío
    def __init__(self):
        self.__products = [] # Lista principal donde se almacenan los productos

    # Método que añade un producto validando que el ID no esté repetido.
    def add_product(self, product):
        for existing_product in self.__products:
            if existing_product.get_product_id() == product.get_product_id():
                return False

        self.__products.append(product)
        return True

    # Método que elimina un producto por su ID
    def remove_product(self, product_id: str):
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                return True
        return False

    # Método que busca productos por su ID
    def find_by_id(self, product_id: str):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    # Método que busca productos por su nombre
    def find_by_name(self, name: str):
        results = []
        for product in self.__products:
            if name.lower() in product.get_name().lower():
                results.append(product)
        return results

    # Método que actualiza la cantidad o precio de un producto por su ID
    def update_product(self, product_id: str, quantity: int = None, price: float = None):
        product = self.find_by_id(product_id)
        if not product:
            return False

        if quantity is not None:
            product.set_quantity(quantity)

        if price is not None:
            product.set_price(price)

        return True
    
    def list_products(self):
        return self.__products
