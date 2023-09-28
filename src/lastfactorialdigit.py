for _ in range(int(input())):
    n = int(input())
    number = 1
    for i in range(1, n + 1):
        number *= i
    print(number % 10)
