productos = []

with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        producto = {
            'nombre': datos[0],
            'precio': float(datos[1]),
            'cantidad': int(datos[2])
        }
        productos.append(producto)

print("Productos actuales:")
for p in productos:
    print(f"{p['nombre']} - ${p['precio']} - {p['cantidad']} unidades")

print("\n=== AGREGAR NUEVO PRODUCTO ===")
nombre = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = int(input("Cantidad: "))

nuevo_producto = {
    'nombre': nombre,
    'precio': precio,
    'cantidad': cantidad
}
productos.append(nuevo_producto)

with open('productos.txt', 'w') as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nProductos guardados exitosamente en productos.txt")