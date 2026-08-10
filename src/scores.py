s = [float(f) for f in input().split()]
if len(s) < 3:
    print("At least 3 scores needed!")
else:
    print(f"Sum of scores (3 lowest removed): {sum(sorted(s)[3:])}")
