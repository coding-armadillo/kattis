import math

for _ in range(int(input())):
    message = input()
    size = int(math.sqrt(len(message)))
    m = []
    for i in range(size):
        m.append(message[i * size : (i + 1) * size])

    ans = []
    for i in range(size - 1, -1, -1):
        for j in range(size):
            ans.append(m[j][i])
    print("".join(ans))
