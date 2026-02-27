"""
Sistema de Gestión de Inventarios en consola.

Este programa permite administrar productos dentro de un inventario,
permitiendo añadir, eliminar, actualizar, buscar y listar productos.

El sistema está estructurado utilizando Programación Orientada a Objetos
y una lista como estructura principal de almacenamiento.
"""
# Importa la clase de servicio del menú
from services.menu import Menu

# Función principal que inicia el programa
def main():
    # Mostrar mensaje de inicio
    print("\n✓ Bienvenido, programa iniciado — cargando inventario y configurando el sistema...")

    menu = Menu() # Crea una instancia de la clase Menu para gestionar la interacción con el usuario
    menu.show_menu() # Llama al método show_menu para mostrar el menú principal y gestionar las opciones seleccionadas por el usuario

# Punto de entrada del programa, que llama a la función main para iniciar el sistema de gestión de inventarios
if __name__ == "__main__":
    main()
