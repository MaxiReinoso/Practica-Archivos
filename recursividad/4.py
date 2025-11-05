def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresa un número decimal: "))

if numero == 0:
    binario = "0"
else:
    binario = decimal_a_binario(numero)

print(f"El número {numero} en binario es: {binario}")