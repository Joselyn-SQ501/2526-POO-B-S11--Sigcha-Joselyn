
# 📦 Sistema Avanzado de Gestión de Inventarios 📄

Este proyecto consiste en un sistema avanzado de gestión de inventarios desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y listas como estructura de datos principal.

El sistema permite administrar productos mediante un menú interactivo en consola e incorpora almacenamiento persistente utilizando un archivo de texto.

En esta versión mejorada se optimizó el uso de colecciones y la organización del proyecto, cumpliendo con los requisitos de un sistema avanzado de inventario.

---

## 🎯 Objetivos del Proyecto

### 💻 Desarrollar un proyecto para gestionar productos dentro de un inventario, aplicando:

- Encapsulamiento
- Métodos Getter y Setter
- Validaciones de datos
- Uso de estructuras de datos primitivas (int, float, ...) y compuestas como colecciones (dict, listas auxiliares)
- Separación por capas (modelo, servicios y archivo principal)
- Persistencia de datos mediante archivos
- Manejo de excepciones

### 🔄 Recuperar automáticamente el inventario

Al iniciar el programa, la clase `Inventory`:

1. Verifica si la carpeta `record` y el archivo `inventory.txt` existeb.
2. Si no existen, los crea automáticamente.
3. Si existen, carga los productos almacenados.
4. Reconstruye el diccionario privado `self.__products`.

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
2526-POO-B-S11--Sigcha-Joselyn/Semana 11/
│
improved_inventory_system/
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
│    └── record/
│        └── inventory.txt  # Archivo donde se almacena los productos
│   
├── main.py                # Ejecutable principal
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
## ⚙️ Uso de colecciones

Ahora,se utiliza un diccionario privado como estructura principal para almacenar productos.
```python
self.__products = {}
```
Donde:

- Clave (key): ID del producto
- Valor (value): Objeto `Product`

Esto permite:

- 🔎 Búsqueda rápida por ID (0(1))
- 🚀 Eliminación más eficiente
- 🔄 Actualización directa sin recorrer toda la colección

El inventario utilizaba anteriormente una lista privada como principal, ahora solo se mantuvo en resultados de la búsqueda por nombres:

```python
results = []
```

Tipos primitivos como (`int`, `float`, `str` para atributos

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

- Ejecución sin que exista la carpeta `record` el archivo `inventory.txt`.
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

Este proyecto permitió aplicar de manera práctica conceptos avanzados de Programación Orientada a Objetos en Python, integrando colecciones eficientes como diccionarios para optimizar la gestión de datos.

La incorporación de almacenamiento persistente, manejo de excepciones, normalización de identificadores y validación anticipada de datos fortaleció la estructura del sistema, haciéndolo más robusto, organizado y escalable.

El sistema demuestra la correcta aplicación de:

- POO
- Colecciones
- Persistencia de datos
- Separación de responsabilidades
- Buenas prácticas de organización y documentación
