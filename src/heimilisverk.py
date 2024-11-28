n = int(input())
l = {}
for _ in range(n):
    s = input()
    if s not in l:
        print(s)
        l[s] = True
