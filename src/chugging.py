n = int(input())
ta, da = [int(d) for d in input().split()]
tb, db = [int(d) for d in input().split()]
a = n * ta + da * (n - 1) * n / 2
b = n * tb + db * (n - 1) * n / 2
if a == b:
    print("=")
elif a < b:
    print("Alice")
else:
    print("Bob")
