winner, max_score = 0, 0
for i in range(5):
    score = sum([int(d) for d in input().split()])
    if score > max_score:
        max_score = score
        winner = i + 1

print(winner, max_score)
