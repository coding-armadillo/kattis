parts = input().split()
l = parts[-1]
f = " ".join([f"{c[0]}." for c in parts[:-1]])
print(f"{l}, {f}" if f else l)
