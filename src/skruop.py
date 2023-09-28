volume = 7
for _ in range(int(input())):
    if input() == "Skru op!":
        volume = min(volume + 1, 10)
    else:
        volume = max(volume - 1, 0)
print(volume)
