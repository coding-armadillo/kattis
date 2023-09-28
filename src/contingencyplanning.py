def permutations(n, c):
    value = 1
    for i in range(n - c + 1, n + 1):
        value *= i
    return value


n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += permutations(n, i)
if ans > 1_000_000_000:
    print("JUST RUN!!")
else:
    print(ans)
