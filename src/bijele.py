should_contain = (1, 1, 2, 2, 2, 8)
found = [int(d) for d in input().split()]
print(" ".join([str(a - b) for a, b in zip(should_contain, found)]))
