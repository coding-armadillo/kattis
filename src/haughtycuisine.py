from random import randint

n = int(input())
menu = []
for _ in range(n):
    menu.append(input().split())

print("\n".join(menu[randint(0, n - 1)]))
