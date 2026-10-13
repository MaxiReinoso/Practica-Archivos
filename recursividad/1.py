def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingresa un número: "))

print(f"\nFactoriales desde 1 hasta {numero}:")
for i in range(1, numero + 1):
    print(f"Factorial de {i}: {factorial(i)}")