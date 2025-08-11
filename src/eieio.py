n = int(input())
m = int(input())
r = m - 2 * n
if r % 2 or r // 2 > n or r < 0:
    print("Rong talning")
else:
    print(r // 2)
