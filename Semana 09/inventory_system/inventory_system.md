# 📦 Sistema de Gestión de Inventarios 📄

Este proyecto consiste en un sistema de gestión de inventarios desarrollado en Python, utilizando Programación Orientada a Objetos (POO) y listas como estructura de datos principal.

El sistema permite administrar productos mediante un menú interactivo en consola.

---

## 🎯 Objetivo del Proyecto

Desarrollar una aplicación modular que permita gestionar productos dentro de un inventario, aplicando:

- Encapsulamiento
- Métodos Getter y Setter
- Validaciones de datos
- Uso de estructuras de datos primitivas (int, float, ...) y compuestas como las listas.
- Separación por capas (modelo, servicios y archivo principal)


## 📂 Estructura del Repositorio
```
2526-POO-Sigcha-Joselyn/Semana 09/
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

En conclusión, este sistema constituye una base sólida para comprender cómo estructurar aplicaciones reales utilizando clases, servicios y mecanismos de validación.
