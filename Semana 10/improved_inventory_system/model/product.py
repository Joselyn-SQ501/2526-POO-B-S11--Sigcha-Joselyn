# Clase que representa un producto del inventario
class Product:
    # Constructor de la clase product con datos
    def __init__(self, product_id: str, name: str, quantity: int, price: float):
        # Atributos privados para aplicar encapsulamiento
        self.__product_id = product_id  # Atributo privado que es el identificador único del producto
        self.__name = name # Atributo privado del nombre del producto
        self.__quantity = quantity # Atributo privado para la cantidad existente del producto
        self.__price = price # Atributo privado del precio del producto.

    # Métodos Getters para acceder y traer información

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_quantity(self) -> int:
        return self.__quantity

    def get_price(self) -> float:
        return self.__price

    # Métodos setter para establecer la información del producto

    def set_name(self, name: str):
        self.__name = name

    def set_quantity(self, quantity: int):
        self.__quantity = quantity

    def set_price(self, price: float):
        self.__price = price

    # Método que devuelve la información establecida del producto
    def get_info(self):
        return f"ID: {self.__product_id} | Nombre: {self.__name} | Cantidad: {self.__quantity} | Precio: ${self.__price:.2f}"

    # Método para imprimir la información del producto
    def print_info(self):
        print(self.get_info())
