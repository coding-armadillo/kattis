_ = input()
p = float(input())
n = int(input())
items = [input() == "ekki plast" for _ in range(n)]
print("Jebb" if sum(items) <= p * n else "Neibb")
