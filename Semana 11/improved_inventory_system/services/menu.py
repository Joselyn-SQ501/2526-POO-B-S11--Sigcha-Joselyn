# Trae el modelo o clase de productos
from model.product import Product
# Trae las clases de servicios correspondientes a inventario y validación
from services.inventory import Inventory
from services.validator import Validator

# Clase menú de servicio que representa la interfaz en consola gestionando la interacción con el usuario
class Menu:
    # Creación de un constructor vacío
    def __init__(self):
        self.inventory = Inventory() # Instancia de la clase Inventory para gestionar el inventario de productos
    
    # Método que muestra el menú principal y gestiona las opciones seleccionadas por el usuario
    def show_menu(self):
        while True:
            print("\n" + "="*50)
            print("📦 SISTEMA DE GESTIÓN DE INVENTARIOS 📄")
            print("="*50)
            print("1. Añadir producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Listar inventario")
            print("6. Salir")
            print("="*50)

            option = input("\nSeleccione una opción: ").strip()

            if option == "1":
                self.add_product()
            elif option == "2":
                self.remove_product()
            elif option == "3":
                self.update_product()
            elif option == "4":
                self.search_product()
            elif option == "5":
                self.list_products()
            elif option == "6": # Condicional para salir del sistema
                print("\nSaliendo del sistema...💻")
                print("✓ ¡Hasta luego👋😺 Gracias por usar el sistema 📄!")
                break
            else:
                print("\n✖️ Opción no válida") # Condicional para manejar opciones no válidas ingresadas por el usuario
    
    # Método que gestiona la adición de un nuevo producto al inventario, solicitando los datos necesarios al usuario y validándolos antes de crear el producto
    def add_product(self):
        product_id = input("Ingrese el ID del producto: ").strip() # Solicita el ID del producto al usuario y valida que no esté vacío
        validate_id, message_id = Validator.validate_id(product_id)
        if not validate_id:
            print(f"✗ Error: {message_id}")
            return
        
        # Solicita el nombre del producto al usuario y valida que no esté vacío y tenga al menos 2 caracteres
        name = input("Ingrese el nombre del producto: ").strip()
        validate_name, message_name = Validator.validate_name(name)
        if not validate_name:
            print(f"✗ Error: {message_name}")
            return
        
        # Solicita la cantidad de productos o unidades existentes al usuario y valida que sea un número entero válido y no negativo
        quantity = input("Ingrese la cantidad de productos o unidades existentes: ").strip()
        validate_quantity, message_quantity = Validator.validate_int(quantity)
        if not validate_quantity:
            print(f"✗ Error: {message_quantity}")
            return

        # Solicita el precio unitario del producto al usuario y valida que sea un número decimal válido y no negativo
        price = input("Ingrese el precio del producto unitariamente: ").strip()
        validate_price, message_price = Validator.validate_float(price)
        if not validate_price:
            print(f"✗ Error: {message_price}")
            return
        
        # Si todas las validaciones son correctas, se crea una nueva instancia de producto con los datos proporcionados por el usuario y se intenta añadir al inventario
        product = Product(product_id, name, int(quantity), float(price))
        
        if self.inventory.add_product(product): # Condicional que verifica si el producto se añadió correctamente al inventario, si es así, se añade al inventario
            print("\n✓ Producto agregado y guardado correctamente en el archivo 🗃️")
            print("\n📌 Información del producto agregado:")
            product.print_info()
        else: # Si el producto no se pudo añadir al inventario, se muestra un mensaje de error indicando que no se añadio porque el ID del producto ya existe
            print(f"\n✗ El ID '{product_id}' ya existe. Verifique los datos ingresados 👀")
    
    # Método que gestiona la eliminación de un producto del inventario, solicitando el ID del producto a eliminar y validándolo antes de intentar eliminarlo del inventario
    def remove_product(self):
        product_id = input("Ingrese el ID del producto a eliminar: ").strip()
        validate_id, message_id = Validator.validate_id(product_id)
        if not validate_id:
            print(f"\n✗ Error: {message_id}")
            return
        # Buscar producto antes de eliminarlo
        product = self.inventory.find_by_id(product_id)

        if product:
            self.inventory.remove_product(product_id)
            print(f"\n✓ Producto '{product.get_product_id()}': '{product.get_name()}' eliminado correctamente del inventario")
        else:
            print(f"\n✗ Producto con ID '{product_id}' no encontrado. Verifique que el ID sea correcto 👀")
    
    # Método que gestiona la actualización de un producto del inventario, solicitando el ID del producto a actualizar y validándolo antes de intentar actualizarlo en el inventario
    def update_product(self):
        product_id = input("Ingrese el ID del producto a actualizar: ").strip()

        # Validar formato del ID
        validate_id, message_id = Validator.validate_id(product_id)
        if not validate_id:
            print(f"\n✗ Error: {message_id}")
            return

        # Verifica si el producto existe antes de pedir nuevos datos
        product = self.inventory.find_by_id(product_id)
        
        # Si el producto no existe, muestra un mensaje de error y retorna para evitar solicitar datos adicionales
        if not product:
            print(f"\n✗ Producto con ID '{product_id}' no encontrado. Verifique que el ID sea correcto 👀")
            return
        
        # Solicita al usuario la nueva cantidad y precio del producto, permitiendo dejar vacío para omitir la actualización de cada campo, y valida los datos ingresados
        quantity = input("Ingrese la nueva cantidad del producto (dejar vacío para omitir): ").strip()
        price = input("Ingrese el nuevo precio del producto por unidad (dejar vacío para omitir): ").strip()
        
        # Valida cantidad si se proporcionó
        new_quantity = int(quantity) if quantity else None
        new_price = float(price) if price else None

        # Se actualiza el producto en el inventario con los nuevos datos proporcionados por el usuario, si se proporcionó una nueva cantidad o precio, se actualiza el producto, de lo contrario, se mantiene el valor actual
        self.inventory.update_product(product_id, new_quantity, new_price) 
        
        # Si la actualización fue exitosa, muestra un mensaje de éxito y la información actualizada del producto
        print(f"\n✓ Producto '{product.get_product_id()}': '{product.get_name()}' actualizado y guardado correctamente en el archivo 🗃️")
        print("\n📌 Información actualizada:")
        product.print_info()

    # Método que gestiona la búsqueda de productos en el inventario, permitiendo al usuario buscar por ID o por nombre, y validando los datos ingresados antes de realizar la búsqueda
    def search_product(self):
        print("\n1. Buscar por ID del producto")
        print("2. Buscar por nombre del producto")
        option_search = input("\nSeleccione una opción: ").strip()
        
        # Condicional que verifica la opción de búsqueda seleccionada por el usuario, solicitando el ID del producto a buscar y se valida antes de realizar la búsqueda por ID en el inventario
        if option_search == "1":
            product_id = input("Ingrese el ID del producto a buscar: ").strip()
            validate_id, message_id = Validator.validate_id(product_id)
            if not validate_id:
                print(f"\n✗ Error: {message_id}")
                return

            product = self.inventory.find_by_id(product_id) 
            
            # Si se encuentra el producto con el ID especificado, se muestra la información del producto encontrado
            if product:
                product.print_info()
            else:
                print(f"\n✗ No existe producto con ID '{product_id}'. Verifique que el ID ingresado sea correcto👀")

        # Condicional que verifica la opción de búsqueda seleccionada por el usuario, solicitando el nombre del producto a buscar y se valida antes de realizar la búsqueda por nombre en el inventario, permitiendo coincidencias parciales y no distinguiendo entre mayúsculas y minúsculas
        elif option_search == "2":
            name = input("Ingrese el nombre del producto a buscar: ").strip()
            validate_name, message_name = Validator.validate_name(name)
            if not validate_name:
                print(f"\n✗ Error: {message_name}")
                return

            results = self.inventory.find_by_name(name)
            # Si se encuentran productos que coinciden con el nombre especificado, se muestra la información de cada producto encontrado
            if results:
                print(f"\n✓ Se encontraron {len(results)} resultado(s):")
                for product in results:
                    product.print_info()
            else:
                print(f"\n✗ No existe producto con nombre '{name}'. Verifique que el nombre ingresado sea correcto👀")
        else:
            print("\n✗ Opción no válida") # Condicional para manejar opciones de búsqueda no válidas ingresadas por el usuario
    
    # Método que lista todos los productos en el inventario, mostrando un mensaje si el inventario está vacío o la información de cada producto si hay productos en el inventario
    def list_products(self):
        products = self.inventory.list_products()
        if products:
            for product in products:
                product.print_info()
        else:
            print("\n📦 El inventario está vacío.")

