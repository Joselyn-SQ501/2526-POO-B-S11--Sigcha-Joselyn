# 📦 Sistema de Gestión de Inventarios 📄

Este proyecto consiste en un sistema de gestión de inventarios desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y listas como estructura de datos principal.

El sistema permite administrar productos mediante un menú interactivo en consola.

Además. en esta versión mejorada del sistema se implementó almacenamiento persistente utilizando un archivo de texto llamado:`inventario.txt`

---

## 🎯 Objetivos del Proyecto

### 💻 Desarrollar un proyecto para gestionar productos dentro de un inventario, aplicando:

- Encapsulamiento
- Métodos Getter y Setter
- Validaciones de datos
- Uso de estructuras de datos primitivas (int, float, ...) y compuestas como las listas.
- Separación por capas (modelo, servicios y archivo principal)

### 🔄 Recuperar automáticamente el inventario

Al iniciar el programa, la clase `Inventory`:

1. Verifica si el archivo `inventario.txt` existe.
2. Si no existe, lo crea automáticamente.
3. Si existe, carga los productos almacenados.
4. Reconstruye la lista privada `self.__products`.

De esta manera, el inventario se mantiene sincronizado entre memoria y archivo.

---

### ⚠️ Manejar excepciones

Para garantizar estabilidad y robustez del sistema, se implementó manejo de excepciones durante la lectura y escritura de archivos.

Se manejan los siguientes casos:

- `FileNotFoundError`: Se crea automáticamente el archivo si no existe.
- `PermissionError`: Se notifica al usuario cuando no existen permisos adecuados.
- `ValueError`: Se detectan y omiten líneas con datos inválidos o corruptos.
- `Exception`: Captura cualquier error inesperado durante la manipulación del archivo.

Esto evita que el programa se cierre abruptamente ante errores y mejora la resiliencia del sistema.

---

### 🔔 Notificar en la Interfaz de Usuario

El menú en consola fue actualizado para informar al usuario sobre:

- Éxito en la escritura del archivo.
- Fallos en el guardado.
- Confirmación de operaciones realizadas correctamente.
- Problemas detectados durante la lectura del archivo.

Esto mejora la experiencia de usuario y permite una interacción más clara con el sistema.

---

## 📂 Estructura del Repositorio
```
2526-POO-Sigcha-Joselyn/Semana 10/
│
inventory_system/
│
│   ├── model/              # Capa de datos, clase product
│   │   └── __init__.py
│   │   └── product.py
│   │
│   └── services/           # Capa de lógica
│    └── __init__.py
│    └── inventory.py
│    └── menu.py
│    └── validator
│   
├── main.py                # Ejecutable principal
├── inventory.txt          # Archivo donde se almacena los productos
└── inventory_system.md    # Documentación del proyecto
```

---

## 📦 Clase Principal: Product

La clase `Product` representa la entidad principal del sistema.

### Atributos privados:
- `product_id` (identificador único)
- `name`
- `quantity`
- `price`

### Métodos:
- Constructor
- Getters
- Setters
---
## ⚙️ Uso de Listas

El inventario utiliza una lista privada:

```python
self.__products = []
```
---

## 🧠 Funcionamiento General

El sistema funciona de la siguiente manera:

1. El usuario interactúa con un menú en consola.
2. Los datos ingresados son validados mediante la clase `Validator`.
3. Se crean objetos de tipo `Product`.
4. Los productos se almacenan en una lista privada dentro de la clase `Inventory`.
5. El sistema permite CRUD del producto y métodos para mostrar información del mismo:
   - Añadir productos (validando que el ID no esté repetido).(append)
   - Eliminar productos por ID (remove)
   - Actualizar productos por ID 
   - Buscar productos por ID o nombre 
   - Listar todos los productos en el inventario
   - Salir del sistema
6. Cada vez que se realiza una operación de:

   - Añadir un producto  
   - Actualizar un producto  
   - Eliminar un producto  

   El sistema reescribe automáticamente el archivo con el inventario actualizado. 
   
   El formato de almacenamiento utilizado es tipo CSV: 
   `id,nombre,cantidad,precio`

   Esto permite que la información se conserve incluso después de cerrar el programa.
---
## 🧪 Pruebas Realizadas

Se realizaron pruebas en los siguientes escenarios:

- Ejecución sin que exista el archivo `inventario.txt`.
- Archivo con líneas corruptas.
- Intento de escritura sin permisos adecuados.
- Persistencia de datos tras cerrar y volver a ejecutar el programa.
- Reversión de cambios en caso de fallo al guardar información.

Los resultados demostraron que el sistema mantiene consistencia entre los datos en memoria y los datos almacenados en el archivo.

---
## 🚀 Cómo Ejecutar el Programa

1. **Clonar el repositorio**:
2. **Abrir en IDE**: Abrir la carpeta raíz en **PyCharm** o **Visual Studio Code**.
3. **Ejecutar**:
    ```bash
    python main.py
    ```
   
## 🏁 Conclusión

Este proyecto permitió aplicar de manera práctica los conceptos de Programación Orientada a Objetos (POO) en Python mediante el desarrollo de un sistema de gestión de inventarios.

Durante su implementación se utilizaron principios fundamentales como el encapsulamiento, la modularidad, la validación de datos y el manejo de listas como estructura principal de almacenamiento. El sistema permite gestionar productos de forma eficiente, incluyendo su creación, actualización, eliminación y búsqueda.

Además, el proyecto refuerza buenas prácticas de programación como la organización del código, la separación de responsabilidades y la interacción clara con el usuario a través de un menú en consola.

También, en esta versión mejorada, se incorporó almacenamiento persistente mediante archivos de texto y manejo de excepciones, fortaleciendo la resiliencia del sistema ante errores y mejorando la consistencia entre los datos en memoria y los datos almacenados externamente. Esto permitió aplicar conceptos fundamentales como manipulación de archivos y control de errores en Python.