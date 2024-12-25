from math import sqrt

def fib(n):
    phi = (1 + sqrt(5)) / 2
    return round(phi**n / sqrt(5))

print(fib(32))  # 2178309
