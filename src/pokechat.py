chars = input()
ids = input()
ids = [int(ids[i : i + 3]) - 1 for i in range(0, len(ids), 3)]
print("".join([chars[i] for i in ids]))
