def score(a, b):
    roll = set([a, b])
    if roll == {1, 2}:
        return (3, None)
    elif len(roll) == 1:
        return (2, a)
    else:
        a, b = min(a, b), max(b, a)
        return (1, 10 * b + a)


while True:
    rolls = [int(d) for d in input().split()]
    if not any(rolls):
        break
    score1 = score(*rolls[:2])
    score2 = score(*rolls[2:])
    if score1 == score2:
        print("Tie.")
    elif score1[0] == score2[0]:
        print(f"Player {1 if score1[1] > score2[1] else 2} wins.")
    else:
        print(f"Player {1 if score1[0] > score2[0] else 2} wins.")
