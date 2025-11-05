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

print("Productos cargados en lista de diccionarios:")
for p in productos:
    print(p)