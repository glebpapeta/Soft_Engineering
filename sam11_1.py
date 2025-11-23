def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib_sequence = fib(200)
    result = list(fib_sequence)[-1]

    print(f"200-е число Фибоначчи: {result}")
