n, k, p = input().split()
n = int(n)
k = int(k)
p = float(p)
ev = n * p - k
if ev < 0:
    print("spela")
else:
    print("spela inte!")
