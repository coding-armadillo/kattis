N, M = input().split()
N = int(N)
M = int(M)

P = [int(t) for t in input().split()]

d = 0
l = 0
for i in range(len(P)):
    if P[i] > N-d:
        break
    if P[i] <= N-d:
        k = P[i]
        d += k
        l += 1

print(M - l)
