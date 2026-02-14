from model.product import Product
from services.inventory import Inventory
from services.validator import Validator



class Menu:
    def __init__(self):
        self.inventory = Inventory()

    def show_menu(self):
        while True:
            print("\n" + "="*50)
            print("📄 SISTEMA DE GESTIÓN DE INVENTARIOS 📄")
            print("="*50)
            print("1. Añadir producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Listar inventario")
            print("6. Salir")
            print("="*50)

            option = input("Seleccione una opción: ").strip()

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
            elif option == "6":
                print("\nSaliendo del sistema...💻")
                print("\n✓ ¡Hasta luego👋😺 Gracias por usar el sistema 📄!")
                break
            else:
                print("✖️ Opción no válida")

    def add_product(self):
        product_id = input("Ingrese el ID del producto: ").strip()
        validate_id, message_id = Validator.validate_id(product_id)
        if not validate_id:
            print(f"✗ Error: {message_id}")
            return
        
        name = input("Ingrese el nombre del producto: ").strip()
        validate_name, message_name = Validator.validate_name(name)
        if not validate_name:
            print(f"✗ Error: {message_name}")
            return

        quantity = input("Ingrese la cantidad de productos o unidades existentes: ").strip()
        validate_quantity, message_quantity = Validator.validate_int(quantity)
        if not validate_quantity:
            print(f"✗ Error: {message_quantity}")
            return

        price = input("Ingrese el precio del producto unitariamente: ").strip()
        validate_price, message_price = Validator.validate_float(price)
        if not validate_price:
            print(f"✗ Error: {message_price}")
            return

        product = Product(product_id, name, int(quantity), float(price))

        if self.inventory.add_product(product):
            print("✓ Producto agregado correctamente")
        else:
            print(f"✗ El ID '{product_id}' ya existe. Verifique los datos ingresados 👀")
    
    def remove_product(self):
        product_id = input("Ingrese el ID del producto a eliminar: ").strip()
        validate_id, message_id = Validator.validate_id(product_id)
        if not validate_id:
            print(f"✗ Error: {message_id}")
            return

        if self.inventory.remove_product(product_id):
            print(f"✓ Producto '{product_id}' eliminado correctamente")
        else:
            print(f"✗ Producto con ID '{product_id}' no encontrado. Verifique que el ID sea correcto 👀")

    def update_product(self):
        product_id = input("Ingrese el ID del producto a actualizar: ").strip()

        # Validar formato del ID
        validate_id, message_id = Validator.validate_id(product_id)
        if not validate_id:
            print(f"✗ Error: {message_id}")
            return

        # Verifica si el producto existe ANTES de pedir nuevos datos
        product = self.inventory.find_by_id(product_id)

        if not product:
            print(f"✗ Producto con ID '{product_id}' no encontrado. Verifique que el ID sea correcto 👀")
            return

        quantity = input("Ingrese la nueva cantidad del producto (dejar vacío para omitir): ").strip()
        price = input("Ingrese el nuevo precio del producto por unidad (dejar vacío para omitir): ").strip()

        new_quantity = int(quantity) if quantity else None
        new_price = float(price) if price else None

        self.inventory.update_product(product_id, new_quantity, new_price)

        print(f"✓ Producto '{product_id}' actualizado correctamente")
        print("📌 Información actualizada:")
        product.print_info()

    def search_product(self):
        print("\n1.Buscar por ID del producto")
        print("2.Buscar por nombre del producto")
        option_search = input("Seleccione una opción: ").strip()
        
        if option_search == "1":
            product_id = input("Ingrese el ID del producto a buscar: ").strip()
            validate_id, message_id = Validator.validate_id(product_id)
            if not validate_id:
                print(f"✗ Error: {message_id}")
                return

            product = self.inventory.find_by_id(product_id)

            if product:
                product.print_info()
            else:
                print(f"✗ No existe producto con ID '{product_id}'. Verifique que el ID ingresado sea correcto👀")

        elif option_search == "2":
            name = input("Ingrese el nombre del producto a buscar: ").strip()
            validate_name, message_name = Validator.validate_name(name)
            if not validate_name:
                print(f"✗ Error: {message_name}")
                return

            results = self.inventory.find_by_name(name)
            if results:
                print(f"✓ Se encontraron {len(results)} resultado(s):")
                for product in results:
                    product.print_info()
            else:
                print(f"✗ No existe producto con nombre '{name}'. Verifique que el nombre ingresado sea correcto👀")
        else:
            print("✗ Opción no válida")
    
    def list_products(self):
        products = self.inventory.list_products()
        if products:
            for product in products:
                product.print_info()
        else:
            print("📦 El inventario está vacío.")

