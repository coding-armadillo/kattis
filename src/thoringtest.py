n = int(input())
w = [input().lower() for _ in range(n)]
s = input().split()
f = True
for t in s:
    if t.lower() not in w:
        f = False
        break
print("Hi, how do I look today?" if f and s else "Thore has left the chat")
