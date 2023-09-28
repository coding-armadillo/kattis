n = int(input())
words = []
for _ in range(n):
    words.append(input())
m = max([len(w) for w in words])
ans = []
for i in range(m):
    values = [ord(w[i]) for w in words if len(w) > i]
    ans.append(sum(values) // len(values))
print("".join(chr(d) for d in ans))
