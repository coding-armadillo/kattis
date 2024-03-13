n = int(input())
s = set()
for _ in range(n):
    s.add(input())
if len(s) == 2:
    print("blandad best")
else:
    print(s.pop())
