numbers = sorted([int(d) for d in input().split()])
orders = list(input())
order_map = {
    "A": 0,
    "B": 1,
    "C": 2,
}

print(" ".join([str(numbers[order_map[o]]) for o in orders]))
