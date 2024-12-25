import time

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def run_fib():
    for n in [5, 10, 15, 20, 32]:
        start_time = time.time()
        result = fib(n)
        elapsed_time = (time.time() - start_time) * 1000  # Время в миллисекундах
        print(f"fib({n}) = {result}, Time: {elapsed_time:.2f} ms")

run_fib()
