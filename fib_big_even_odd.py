def fib_eo(n):
    a, b = 0, 1
    for _ in range(n % 60):  # Повторение чисел Фибоначчи по модулю 10 каждые 60 чисел
        a, b = b, (a + b) % 10
    return "even" if a % 2 == 0 else "odd"

print(fib_eo(841645))  # odd
