# Menú de productos
menu = ["Pizza", "Hamburguesa", "Ensalada", "Refresco", "Papas", "Postre"]

# Precios del menú
precios_menu = {
    "Pizza": 125.0,
    "Hamburguesa": 20.0,
    "Ensalada": 8.0,
    "Refresco": 3.0,
    "Papas": 4.0,
    "Postre": 10.0
}

# Categorías de productos
categorias_menu = {
    "Pizza": "Comida",
    "Hamburguesa": "Comida",
    "Ensalada": "Comida",
    "Refresco": "Bebida",
    "Papas": "Comida",
    "Postre": "Postre"
}

# Lista para guardar los pedidos del cliente
pedidos = []

print("¡Bienvenido a la tienda online!")
print("Escriba el nombre del producto para agregarlo a su pedido.")
print("Escriba 'salir' cuando haya terminado.\n")

# Bucle para tomar pedidos
while True:
    print("Menú disponible:")
    for producto in menu:
        print(f"- {producto}: ${precios_menu[producto]:.2f}")

    eleccion = input("¿Qué desea ordenar? ").title()

    if eleccion == "Salir":
        break
    elif eleccion in menu:
        pedidos.append(eleccion)
        print(f"{eleccion} agregado a su pedido.")
    else:
        print("Producto no válido. Por favor, elija uno del menú.")

# Verificar si se pidió al menos un producto
if not pedidos:
    print("No se realizó ningún pedido.")
else:
    # Calcular total y contar productos
    total_original = 0
    conteo_productos = {}
    categorias_pedidas = set()

    for producto in pedidos:
        total_original += precios_menu[producto]
        conteo_productos[producto] = conteo_productos.get(producto, 0) + 1
        categorias_pedidas.add(categorias_menu[producto])

    # Calcular descuento
    descuento = 0

    if total_original > 50:
        descuento = total_original * 0.10
    elif total_original > 30:
        descuento = total_original * 0.05

    total_final = total_original - descuento

    # Mostrar resumen del pedido
    print("--- Resumen del pedido ---")
    for producto, cantidad in conteo_productos.items():
        print(f"{producto}: {cantidad} unidad(es)")

    print("Categorías de productos pedidos:")
    for categoria in categorias_pedidas:
        print(f"- {categoria}")

    print(f"Total original: ${total_original:.2f}")
    print(f"Descuento aplicado: ${descuento:.2f}")
    print(f"Total a pagar: ${total_final:.2f}")
    print("¡Gracias por su compra!")
