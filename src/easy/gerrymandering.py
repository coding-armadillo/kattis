p, _ = [int(d) for d in input().split()]
votes = {}
for _ in range(p):
    d, a, b = [int(d) for d in input().split()]
    if d not in votes:
        votes[d] = {"A": a, "B": b}
    else:
        votes[d]["A"] += a
        votes[d]["B"] += b

total_wa, total_wb = 0, 0
for d in sorted(votes):
    total = votes[d]["A"] + votes[d]["B"]
    t = total // 2 + 1
    winner = "A" if votes[d]["A"] > votes[d]["B"] else "B"
    wa = votes[d]["A"] - t if votes[d]["A"] > votes[d]["B"] else votes[d]["A"]
    wb = votes[d]["B"] - t if votes[d]["B"] > votes[d]["A"] else votes[d]["B"]
    print(winner, wa, wb)
    total_wa += wa
    total_wb += wb
v = sum([sum(ab.values()) for ab in votes.values()])
print(abs(total_wa - total_wb) / v)
