# Clase que representa un proveedor
class Supplier:
    # Constructor de la clase Supplier con datos
    def __init__(self, supplier_id: str, name: str, product_type: str, email: str, phone: int):
        # Atributos privados para aplicar encapsulamiento
        self.__supplier_id = supplier_id # Atributo privado que es el identificador único del proveedor
        self.__name = name # Atributo privado del nombre del proveedor
        self.__product_type = product_type # Atributo privado del tipo de producto que abastece el proveedor
        self.__email = email # Atributo privado del correo del proveedor
        self.__phone = phone # Atributo privado del teléfono del proveedor

    # Métodos Getters para acceder y traer información

    def get_id(self) -> str:
        return self.__supplier_id

    def get_name(self) -> str:
        return self.__name

    def get_product_type(self) -> str:
        return self.__product_type

    def get_email(self) -> str:
        return self.__email

    def get_phone(self) -> int:
        return self.__phone

    # Métodos setter para establecer la información del proveedor

    def set_name(self, name: str):
        self.__name = name

    def set_product_type(self, product_type: str):
        self.__product_type = product_type

    def set_email(self, email: str):
        self.__email = email

    def set_phone(self, phone: int):
        self.__phone = phone

    # Método que devuelve la información establecida del proveedor
    def get_info_supplier(self):
        return f"ID: {self.__supplier_id} | Nombre: {self.__name} | Contacto: {self.__product_type} | Email: {self.__email} | Tel: {self.__phone}"

    # Método para imprimir la información del proveedor
    def print_info_supplier(self):
        print(self.get_info_supplier())
