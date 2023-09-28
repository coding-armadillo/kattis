s = set(input())
m = input().split()
print(" ".join(["*" * len(p) if s & set(p) else p for p in m]))
