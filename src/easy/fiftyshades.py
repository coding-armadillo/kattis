total = 0
for _ in range(int(input())):
    button = input().lower()
    if "pink" in button or "rose" in button:
        total += 1
if not total:
    print("I must watch Star Wars with my daughter")
else:
    print(total)
