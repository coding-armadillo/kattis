tb, lr = 0, 0
for _ in range(int(input())):
    s = input()
    tb += s[:2].count("0")
    lr += s[2:].count("0")

swords = min(tb, lr) // 2
tb -= swords * 2
lr -= swords * 2

print(f"{swords} {tb} {lr}")
