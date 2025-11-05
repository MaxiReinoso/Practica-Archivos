def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingresa un número entero positivo: "))

resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es: {resultado}")