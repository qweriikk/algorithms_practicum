import time

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def run_fib_recursive():
    for n in [5, 10, 15, 20, 24]:
        start_time = time.time()
        result = fib(n)
        elapsed_time = (time.time() - start_time) * 1000 
        print(f"fib({n}) = {result}, Time: {elapsed_time:.2f} ms")
    print("Сложность алгоритма: экспоненциальная (O(2^n)).")

run_fib_recursive()
