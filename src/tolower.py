p, t = [int(d) for d in input().split()]
score = 0
for _ in range(p):
    solved = True
    for _ in range(t):
        s = input()
        if solved:
            s = s[0].lower() + s[1:]
            if s.lower() == s:
                continue
        solved = False
    if solved:
        score += 1
print(score)
