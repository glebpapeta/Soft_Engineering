def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    with open('fib.txt', 'w', encoding='utf-8') as file:
        for i, num in enumerate(fib(200), 1):
            file.write(f"{num}\n")
            print(f"Записано {i}-е число: {num}")

    fib_generator = fib(200)
    fib_200 = None
    for num in fib_generator:
        fib_200 = num

    print(f"\n200-е число Фибоначчи: {fib_200}")
    print("Все числа записаны в файл 'fib.txt'")
