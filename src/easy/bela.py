table = {
    "A": {True: 11, False: 11},
    "K": {True: 4, False: 4},
    "Q": {True: 3, False: 3},
    "J": {True: 20, False: 2},
    "T": {True: 10, False: 10},
    "9": {True: 14, False: 0},
    "8": {True: 0, False: 0},
    "7": {True: 0, False: 0},
}

n, b = input().split()
n = int(n)
total = 0

for _ in range(4 * n):
    card = input()
    f, s = card[0], card[1]
    total += table[f][s == b]

print(total)
