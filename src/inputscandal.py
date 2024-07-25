lines = []
while True:
    try:
        lines.append(input())
    except:
        break
print(len(lines))
print("\n".join(lines))
