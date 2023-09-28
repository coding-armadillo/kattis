y = int(input())
print("YES" if 26 - ((y - 2018) * 12 - 4) % 26 <= 12 else "NO")
