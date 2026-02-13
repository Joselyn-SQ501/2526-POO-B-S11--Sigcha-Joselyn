# Clase que representa la tienda
class Store:
    # Constructor de la clase Store con datos
    def __init__(self, name: str, location: str, owner: str, email: str, phone: int):
        # Atributos privados para aplicar encapsulamiento
        self.__name = name # Atributo privado del nombre de la tienda
        self.__location = location  # Atributo privado de la ubicación de la tienda
        self.__owner = owner  # Atributo privado del propietario de la tienda
        self.__email = email  # Atributo privado del correo de la tienda
        self.__phone = phone  # Atributo privado del teléfono de la tienda

    # Métodos Getters para acceder y traer el nombre de la tienda
    def get_name(self) -> str:
        return self.__name

    # Método setter para establecer el nombre de la tienda
    def set_name(self, name: str):
        self.__name = name

    # Método que devuelve la información de la tienda
    def get_info_store(self):
        return f"Tienda: {self.__name}\nUbicación: {self.__location}\nPropietario: {self.__owner}\nEmail: {self.__email}\nTeléfono: {self.__phone}"

    # Método para imprimir la información de la tienda
    def print_info_store(self):
        print("\n" + "-"*50)
        print(self.get_info_store())
        print("-"*50)
