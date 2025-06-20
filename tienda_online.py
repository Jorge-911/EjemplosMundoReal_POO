# tienda_online.py

"""
Este ejemplo representa una situación del mundo real: una tienda en línea.
Utiliza Programación Orientada a Objetos (POO) para modelar productos, clientes y la lógica de compra.
Incluye interacción entre clases, atributos y métodos definidos, aplicando los principios de la POO.
"""

# ----------------------------
# Clase Producto
# ----------------------------
class Producto:
    """
    Clase que representa un producto de la tienda.
    Atributos:
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        """
        Muestra la información del producto (nombre y precio).
        """
        print(f"Producto: {self.nombre} - Precio: ${self.precio}")

# ----------------------------
# Clase Cliente
# ----------------------------
class Cliente:
    """
    Clase que representa un cliente.
    Atributos:
        nombre (str): Nombre del cliente.
        carrito (list): Lista de productos agregados al carrito.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_producto(self, producto):
        """
        Agrega un producto al carrito del cliente.
        """
        self.carrito.append(producto)
        print(f"{producto.nombre} agregado al carrito de {self.nombre}")

    def ver_carrito(self):
        """
        Muestra todos los productos en el carrito del cliente.
        """
        print(f"\nCarrito de {self.nombre}:")
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            for p in self.carrito:
                p.mostrar_info()

    def calcular_total(self):
        """
        Calcula y muestra el total a pagar por los productos en el carrito.
        """
        total = sum(p.precio for p in self.carrito)
        print(f"Total a pagar: ${total:.2f}")

# ----------------------------
# Ejecución del programa
# ----------------------------
if __name__ == "__main__":
    # Crear productos (objetos de la clase Producto)
    prod1 = Producto("Camisa", 25.50)
    prod2 = Producto("Pantalón", 40.00)
    prod3 = Producto("Zapatos", 60.00)

    # Crear cliente (objeto de la clase Cliente)
    cliente = Cliente("Laura")

    # Interacción entre objetos: agregar productos al carrito del cliente
    cliente.agregar_producto(prod1)
    cliente.agregar_producto(prod2)
    cliente.agregar_producto(prod3)

    # Mostrar contenido del carrito
    cliente.ver_carrito()

    # Calcular y mostrar total a pagar
    cliente.calcular_total()