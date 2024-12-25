from math import sqrt

def fib_binet(n):
    phi = (1 + sqrt(5)) / 2
    return round(phi**n / sqrt(5))

print(fib_binet(32))  # 2178309
