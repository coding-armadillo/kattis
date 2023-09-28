scores = input()
size = len(scores)
a = sum([int(scores[i + 1]) for i in range(size) if scores[i] == "A"])
b = sum([int(scores[i + 1]) for i in range(size) if scores[i] == "B"])
if a > b:
    print("A")
else:
    print("B")
