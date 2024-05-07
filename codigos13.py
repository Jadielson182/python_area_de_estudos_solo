# Calculando fatorial com recursivas

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
print(factorial(4))
print(factorial(0))