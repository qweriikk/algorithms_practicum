def fib_array(n):
    fib_numbers = [0, 1]
    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])
    return fib_numbers

print(fib_array(8))  # [0, 1, 1, 2, 3, 5, 8, 13, 21]
