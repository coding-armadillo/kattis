from collections import Counter

d = 1
while True:
    try:
        s = input().split()

        if "OPEN" in s:
            book = {}
            t = Counter()
        elif "ENTER" in s:
            book[s[1]] = int(s[2])
        elif "EXIT" in s:
            t[s[1]] += int(s[2]) - book.pop(s[1])
        elif "CLOSE" in s:
            print(f"Day {d}")
            for k in sorted(t):
                print(f"{k} ${t[k]/10:.2f}")
            print()
            d += 1
    except:
        break
