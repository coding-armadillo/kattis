from itertools import permutations

x = input()

values = sorted(set([int("".join(v)) for v in permutations(x, len(x))]))

index = values.index(int(x))
if index + 1 < len(values):
    print(values[index + 1])
else:
    print(0)
