with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.strip().split(',')
        nombre = datos[0]
        precio = datos[1]
        cantidad = datos[2]
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

print("\n=== AGREGAR NUEVO PRODUCTO ===")
nombre = input("Nombre del producto: ")
precio = input("Precio: ")
cantidad = input("Cantidad: ")

with open('productos.txt', 'a') as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print(f"Producto '{nombre}' agregado exitosamente.")