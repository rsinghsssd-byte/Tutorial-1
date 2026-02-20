def fibonacci(n):
    a, b = 0, 2
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
