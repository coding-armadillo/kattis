problems = {}
solved = set()
while True:
    line = input()
    if line == "-1":
        break
    t, p, ans = line.split()
    t = int(t)
    if p in solved:
        continue
    if p not in problems:
        problems[p] = [(t, ans)]
    else:
        problems[p].append((t, ans))
    if ans == "right":
        solved.add(p)

score = 0
for p in problems:
    t, ans = problems[p][-1]
    if ans == "right":
        score += t + 20 * len(problems[p][:-1])

print(len(solved), score)
