# Clase que representa un producto del inventario.
class Product:
    def __init__(self, id="", nombre="", cantidad=0, precio=0.0):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    
    def _obtener_informacion(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
    
    def imprimir(self):
        print(f"  {self._obtener_informacion()}")
