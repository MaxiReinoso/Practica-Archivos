def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

bloques_base = int(input("Ingresa el número de bloques en el nivel más bajo: "))

total = contar_bloques(bloques_base)
print(f"Total de bloques necesarios para construir la pirámide: {total}")