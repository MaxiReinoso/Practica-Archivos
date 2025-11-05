def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingresa el dígito a contar (0-9): "))

resultado = contar_digito(numero, digito)
print(f"El dígito {digito} aparece {resultado} veces en {numero}")