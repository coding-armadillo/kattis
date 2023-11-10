mapping = {
    ".": 20,
    "O": 10,
    "\\": 25,
    "/": 25,
    "A": 35,
    "^": 5,
    "v": 22,
}
n, _ = input().split()
cost = 0
for _ in range(int(n)):
    for c in input():
        cost += mapping[c]
print(cost)
