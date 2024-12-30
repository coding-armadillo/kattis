n = int(input())
s = [(n - int(input())) % 2 for _ in range(n)]
print("Ja" if any(s) else "Nej")
