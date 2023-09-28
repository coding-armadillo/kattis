for _ in range(int(input())):
    words = input().split()
    others = set()
    while True:
        line = input()
        if line == "what does the fox say?":
            break
        w = line.split()[-1]
        others.add(w)
    print(" ".join(w for w in words if w not in others))
